def bubble_sort(lista):
    n = len(lista)
    #Percorre todos os elementos da lista
    for i in range(n):
        #Últimos i elementos já ordenados, então não precisamos considerá-los
            for j in range(0, n-i-1):
                  #Troca se o elemento encontrado se for maior que o proximo elemento
                    if lista[j] > lista[j+1]:
                           lista[j], lista[j+1] = lista[j+1], lista[j]

medicamentos = ['B-Suprin', 'Gaballon', 'Halo','Kaletra','Labcaína Geleia 2%','Amoxicilina','NEOPet']

print(medicamentos) #escreve a lista desorganizada

bubble_sort(medicamentos) #organiza a lista

print(medicamentos) #escreve a lista organizada, pós bubble sort