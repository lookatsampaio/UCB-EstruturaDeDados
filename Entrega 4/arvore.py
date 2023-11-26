class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item
def esq_dir(root): #definimos o tipo de leitura para da esquerda para direita (Inorder Tranversal)
    if root:
        esq_dir(root.left)
        print(str(root.val) + "->", end='')
        esq_dir(root.right)
def sub_top(root): #definimos o tipo de leitura de baixo para o topo (Postorder Tranversal)
    if root:
        sub_top(root.left)
        sub_top(root.right)
        print(str(root.val) + "->", end='')
def top_sub(root): #definimos o tipo de leitura do topo para baixo (Preorder Tranversal)
    if root:
        print(str(root.val) + "->", end='')
        top_sub(root.left)
        top_sub(root.right)

root = Node('B-Suprin') #definimos o produto como a raiz da arvore
root.left = Node('Amoxicilina') #definimos o produto como o galho esquerdo de B-Suprin
root.right = Node('NEOPet') #definimos o produto como o galho direito de B-Suprin
root.left.left = Node('Halo') #definimos o produto como o galho esquerdo de Amoxilina
root.left.right = Node('Gaballon') #definimos o produto como o galho direito de Amoxilina

print("Da esquerda para direita:") #leitura em Inorder Tranversal
esq_dir(root)
print("\n\nDo topo para baixo") #leitura em Preorder Tranversal
top_sub(root)
print("\n\nDe baixo para cima") #leitura em Postorder Tranversal
sub_top(root)