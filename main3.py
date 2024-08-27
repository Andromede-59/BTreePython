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

print("Arbre final : ", t.linearise())

t.suppression(10)
print("suppression 10 : ", t.linearise())

t.suppression(3)
print("suppression 3 : ",t.linearise())

t.suppression(8)
print("suppression 8 : ",t.linearise())

t.suppression(6)
print("suppression 6 : ",t.linearise())

t.suppression(9)
print("suppression 9 : ",t.linearise())

