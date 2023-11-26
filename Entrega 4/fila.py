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
q.enfileirar('Cliente 1')
q.enfileirar('Cliente 2')
q.enfileirar('Cliente 3')
q.enfileirar('Cliente 4')
q.enfileirar('Cliente 5')#adiciona 5 clientes diferentes na fila

print("Clientes da Farmacia na fila:")
q.mostrar()

q.desenfileirar()

print("Cliente atendido!\nAinda na fila:")
q.mostrar()