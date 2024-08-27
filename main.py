from BTree import BTree
from Node import Node
# creation of root
t = BTree(2)
root = Node(False, 2, [6])

#creation of left branch
x4 = Node( False,2, [4])
x3 = Node( True,2,[3])
x5 = Node(True,2,[5])
x4.children = [x3, x5]

#creation of right branch
x8 = Node(   False,2,[8])
x7 = Node(  True,2,[7])
x9a10 = Node(  True,2,[9,10])
x8.children = [x7, x9a10]

#adding root to the tree
root.children = [x4, x8]
t.root = root

# recherche = int(input("Enter the number to search\n"))
print(t.recherche(2))
print(t.recherche(5))
print(t.recherche(8))
print(t.recherche(12))

print(t.linearise())
