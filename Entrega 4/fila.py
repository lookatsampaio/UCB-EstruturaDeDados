class Queue:
    def __init__(self):
        self.queue = []
    def enfileirar(self, item): #adicionar elemento na fila
        self.queue.append(item)
    def desenfileirar(self):     # remover elemento da fila
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def mostrar(self): #escreve a fila
        print(self.queue)


q = Queue()
q.enfileirar("Kaletra")
q.enfileirar("Labcaína Geleia 2%")
q.enfileirar("Amoxicilina")
q.enfileirar("NEOPet") #adiciona os seguintes produtos no carrinho do cliente

print("Produtos a comprar:")
q.mostrar()

q.desenfileirar()

print("Produto registrado na compra!\nA validar:")
q.mostrar()