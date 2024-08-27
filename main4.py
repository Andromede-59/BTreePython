from graphviz import Digraph

def draw_binary_tree(root):
    dot = Digraph(format='png')

    def add_nodes_edges(node, parent_name=None):
        if node is None:
            return
        node_name = str(id(node))
        dot.node(node_name, label=str(node.key))
        if parent_name is not None:
            dot.edge(parent_name, node_name)
        add_nodes_edges(node.left, node_name)
        add_nodes_edges(node.right, node_name)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True)

from BTree import BTree
# creation of root
t = BTree(2)

t.insertion(6)
t.insertion(4)
t.insertion(3)
t.insertion(5)
t.insertion(8)
t.insertion(7)
t.insertion(9)
t.insertion(10)

t.suppression(10)
t.suppression(3)
t.suppression(8)
t.suppression(6)
t.suppression(9)



draw_binary_tree(t)