class Node:
    def __init__(self, leaf, k, keys = None):
        self.k = k
        self.leaf = leaf
        if (keys == None):
            self.keys = []
        else: 
            self.keys = keys
        self.children = []
        self.parent = None

    def insertion_node(self, value):
        res = None
        # Trouve bon index
        i = 0
        while (i < len(self.keys) and value > self.keys[i]):
            i += 1
        # cas feuille
        if (self.leaf): 
            self.keys.insert(i, value)
            # Si trop de clés dans le noeud, split et retourne l'enfant gauche 
            if (len(self.keys)>self.k):
                res = self.split()
        # cas Noeud 
        else:   
            res = self.children[i].insertion_node(value) # On insert jusqu'a trouver une feuille 
            if (res is not None):
                #si noeud pas rempli -> ajoute simplement
                if (len(self.keys)<self.k):   
                    self.keys.insert(i, res[1])
                    self.children.insert(i + 1, res[0])
                    res = None
                # Sinon insert la clé et le nouvel enfant puis split le noeud
                else:   
                    self.keys.insert(i, res[1])
                    self.children.insert(i + 1, res[0])
                    res = self.split()
        # On retourne la valeur finale
        return res
    

    def split(self):
        # On créé le nouveau noeud parent
        new_node = Node(self.leaf, self.k)
        new_node.parent = self.parent
        # On attribut les valeurs (clés) a chaque noeud : le nouveau parent et ses enfants
        key_median = self.keys[self.k//2]    
        new_node.keys = self.keys[self.k//2+1:]
        self.keys = self.keys[:self.k//2]
        # Si notre noeud n'est pas une feuille, alors on redistribue les enfants du noeud précédent
        if (not self.leaf): 
            new_node.children = self.children[self.k//2+1:]
            self.children = self.children[:self.k//2+1]
        # On retourne et le nouveau noeud et la valeur car on souhaite tout avoir dans insertion
        return new_node, key_median