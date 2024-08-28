from BTree import BTree
from graphicsLib import draw_binary_tree
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

draw_binary_tree(t.root)