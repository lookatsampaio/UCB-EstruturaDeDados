class Node:
    def __init__(self, item): # Cria um Node
        self.item = item
        self.next = None
class LinkedList: #Cria a lista encadeada
    def __init__(self):
        self.head = None
if __name__ == '__main__':
    linked_list = LinkedList()      #Insere os elementos (medicamentos) dentro da lista
    linked_list.head = Node("G500 Balsâmico\n") 
    second = Node("Gabalgin\n")
    third = Node("Gabapentina\n")
    fourth = Node("Gabaneurin\n")

    linked_list.head.next = second #conecta os elemntos da lista
    second.next = third
    third.next = fourth

    print("Medicamentos com a Letra G Disponíveis:") #escreve os itens da lista
    while linked_list.head != None:
        print(linked_list.head.item, end="")
        linked_list.head = linked_list.head.next