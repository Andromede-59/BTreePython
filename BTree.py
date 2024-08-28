from Node import Node

class BTree:
    def __init__(self, k, init_node=None):
        self.k = k
        self.L = k // 2 + 1  # minimum number of children
        self.U = k + 1  # maximum number of children
        self.root = None

    def insertion(self, key):
        if (self.root is None):
            self.root = Node(True, self.k)
        if self.recherche(key):
            print(f'{key} is already in the Tree !')
            return
        
        node = self.root.insertion_node(key) #(nnode,nvalue) nor working cuz of none
        
        if (node is not None):  #appel seulement quand il faut "tourner"
            self.change_root(node[0], node[1])

        if len(self.root.children) == 0:
            self.root.leaf = True      

    def suppression(self, cle):
        if not self.recherche(cle):
            print(cle," n'est pas dans l'arbre.")
            return

        self.supprimer_cle(self.root, cle)


        # Vérifier les conditions spécifiées
        if len(self.root.keys) < 1:
            if len(self.root.children) > 0:
                self.root = self.root.children[0]
                self.root.parent = None
                if len(self.root.keys) > self.k:
                    res = self.root.split()
                    if res is not None:
                        self.change_root(res[0], res[1])
            else:
                self.root = None

    def supprimer_cle(self, node, cle):
        i = 0
        while i < len(node.keys) and cle > node.keys[i]:
            i += 1

        if i < len(node.keys) and cle == node.keys[i]:  # Vérifier que i est valide
            if node.leaf:
                del node.keys[i]
            else:
                
                if len(node.children[i].keys) >= self.L:
                    # On trouve la plus grande clé dans le sous-arbre gauche
                    max_key = node.children[i].keys[-1]
                    node.keys[i] = max_key
                    self.supprimer_cle(node.children[i], max_key)
                elif len(node.children[i + 1].keys) >= self.L:
                    # On trouve la plus petite clé dans le sous-arbre droit
                    min_key = node.children[i + 1].keys[0]
                    node.keys[i] = min_key
                    self.supprimer_cle(node.children[i + 1], min_key)
                else:
                    # Fusionner les deux sous-arbres
                    self.fusionner_noeuds_enfants(node, i)
                    self.supprimer_cle(node, cle)
        else:
            # La clé n'est pas dans ce nœud, donc on poursuit la recherche dans le bon enfant
            if not node.leaf:
                self.supprimer_cle(node.children[i], cle)
        
        # Vérifier si le nœud a trop peu de clés après la suppression
        if len(node.keys) < self.L - 1 and node != self.root:
            self.reorganiser_noeud(node)

    def reorganiser_noeud(self, node):
        parent = node.parent
        index = parent.children.index(node)
        left_sibling = None
        right_sibling = None
        if index > 0:
            left_sibling = parent.children[index - 1]
        if index < len(parent.children) - 1:
            right_sibling = parent.children[index + 1]

        # Fusionner avec un frère s'il en a un avec assez de clés
        if left_sibling and len(left_sibling.keys) > self.L - 1:
            self.fusionner_noeuds_enfants(parent, index - 1)

        elif right_sibling and len(right_sibling.keys) > self.L - 1:
            self.fusionner_noeuds_enfants(parent, index)
        else:
            # Fusionner avec un frère et la clé du parent
            if left_sibling:
                self.fusionner_noeuds_enfants(parent, index - 1)
                # parent.keys.pop(index - 1)
            elif right_sibling:
                self.fusionner_noeuds_enfants(parent, index)
                parent.keys.pop(index)
            # Vérifier si le parent a des clés après la suppression
            if parent.keys and len(parent.keys) < self.L - 1 and parent != self.root:
                self.reorganiser_noeud(parent)

    def fusionner_noeuds_enfants(self, parent, index):
        child = parent.children[index]
        left_sibling = None
        right_sibling = None

        if index > 0:
            left_sibling = parent.children[index - 1]
        if index < len(parent.children) - 1:
            right_sibling = parent.children[index + 1]
        
        if left_sibling and len(left_sibling.keys) > self.L - 1:
            # Fusionner avec le frère de gauche
            child.keys.insert(0, parent.keys[index - 1])
            parent.keys[index - 1] = left_sibling.keys.pop(-1)
            if not child.leaf:
                child.children.insert(0, left_sibling.children.pop(-1))
        elif right_sibling and len(right_sibling.keys) > self.L - 1:
            # Fusionner avec le frère de droite
            child.keys.append(parent.keys[index])
            parent.keys[index] = right_sibling.keys.pop(0)
            if not child.leaf:
                child.children.append(right_sibling.children.pop(0))
        else:
            # Fusionner avec le frère de gauche
            if left_sibling:
                left_sibling.keys.append(parent.keys.pop(index - 1))
                left_sibling.keys.extend(child.keys)
                if not child.leaf:
                    left_sibling.children.extend(child.children)
                parent.children.pop(index)
            # Fusionner avec le frère de droite
            elif right_sibling:
                child.keys.append(parent.keys.pop(index))
                child.keys.extend(right_sibling.keys)
                if not child.leaf:
                    child.children.extend(right_sibling.children)
                parent.children.pop(index + 1)
                
                
            # Mise à jour des clés du parent après la fusion
            if left_sibling and right_sibling:
                parent.keys = left_sibling.keys + right_sibling.keys
            elif left_sibling and len(left_sibling.keys)!=0:
                parent.keys = left_sibling.keys
            elif right_sibling and len(right_sibling.keys)!=0:
                parent.keys = right_sibling.keys


        # Si le parent devient trop petit, continuer à réorganiser
        if len(parent.keys) < self.L - 1 and parent != self.root:
            self.reorganiser_noeud(parent)

    def change_root(self, new_node, value):
        old_node = self.root #on stocke le noeud
        self.root = Node(False, self.k) # on créé la nouvelle racine
        # On insert les nouvelles valeurs et l'ancien  noeud dans la nouvelle racine
        self.root.keys.append(value) 
        self.root.children.append(old_node)
        self.root.children.append(new_node)
        self.root.parent = None
        for child in self.root.children:
            child.parent = self.root


    def recherche(self, key, act_node=None):   
        if act_node is None:
            act_node = self.root
        if key in act_node.keys:
            return True
        elif act_node.leaf:
            return False
        else:
            i = 0
            while i < self.k and i<len(act_node.keys) and key > act_node.keys[i]:
                i += 1
            return self.recherche(key, act_node.children[i])

    def print_Tree(self, start_node = None):
        if start_node == None:
            start_node = self.root
        if start_node.leaf:
            return "F" + str(start_node.keys)
        else:
            children = ', '.join(self.print_Tree(child) for child in start_node.children)
            return f'[B{start_node.keys} [{children}]]'
        
    def height(self,node):
        return 1+max([self.height(child) for child in node.children]or [0])
      
    # Pas utilisée ici car retranscrite dans le code directement.
    def is_btree(self, node):
        if len(node.keys) < self.L - 1 or len(node.keys) > self.U - 1 or self.height(node.children[0]) != self.height(node.children[1]):
            return False
        for child in node.children:
            if not self.is_btree(child):
                return False
        return True

