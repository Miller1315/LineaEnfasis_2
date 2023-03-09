class Node:
    def __init__(self, value):
        self.value = value #raiz, el valor del nodo
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

#Crear Arbol
root = Node('A')
root.left = Node('B')
root.right = Node('C')  
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')#######

root.left.left.left = Node('H')
root.left.left.right = Node('I')
root.left.right.left = Node('J')
root.left.right.right = Node('K')

root.right.left.left = Node('L')
root.right.left.right = Node('M')
root.right.right.left = Node('N')
root.right.right.right = Node('O')


print("Recorrido Preorden")
preorder(root)

print("\n Recorrido Postorden")
postorder(root)

print("\n Recorrido inorder")
inorder(root)


