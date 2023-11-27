class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class ListaCircular:
    def __init__(self):
        self.last = None
    def addVazio(self, data): #adiciona o novo elemnto na lista circular vazia
        if self.last != None:
            return self.last
        novoNode = Node(data)
        self.last = novoNode
        self.last.next = self.last
        return self.last
    
    def addFrente(self, data):
        if self.last == None:
            return self.addVazio(data)
        novoNode = Node(data)
        novoNode.next = self.last.next
        self.last.next = novoNode
        return self.last
    
    def addFinal(self, data):
        if self.last == None:
            return self.addVazio(data)
        novoNode = Node(data)
        novoNode.next = self.last.next
        self.last.next = novoNode
        self.last = novoNode
        return self.last

    def addPos(self, data, item):
        if self.last == None:
            return None
        novoNode = Node(data)
        p = self.last.next
        while p:
            if p.data == item:
                novoNode.next = p.next
                p.next = novoNode
                if p == self.last:
                    self.last = novoNode
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print(item, "O medicamento não está presente na lista")
                break

    def apagar(self, last, key):
        if last == None:
            return
        if (last).data == key and (last).next == last:
            last = None
        temp = last
        d = None
        if (last).data == key:
            while temp.next != last:
                temp = temp.next
            temp.next = (last).next
            last = temp.next
        while temp.next != last and temp.next.data != key:
            temp = temp.next
        if temp.next.data == key:
            d = temp.next
            temp.next = d.next
        return last
    
    def traverse(self):
        if self.last == None:
            print("A lista está vazia")
            return
        novoNode = self.last.next
        while novoNode:
            print(novoNode.data, end=" ")
            novoNode = novoNode.next
            if novoNode == self.last.next:
                break

if __name__ == "__main__": #codigo principal
    lc = ListaCircular()
    last = lc.addVazio("G500 Balsâmico") #adiciona o medicamento inicial já que lista está vazia
    last = lc.addFinal("Gabalgin") #adiciona o medicamento na posição final da lista
    last = lc.addFrente("Gabapentina") #adiciona o medicamento na primeira posição da lista
    last = lc.addPos("Gabaneurin", "Gabapentina") #adiociona o medicamento após o elemento "Gabantina"
    last = lc.addFinal("Amoxilicina") #adiciona o medicamento na nova posição final da lista
    lc.traverse()
    last = lc.apagar (last, "Gabapentina")
    print("\nMedicamentos após exclusão:")
    lc.traverse()
   