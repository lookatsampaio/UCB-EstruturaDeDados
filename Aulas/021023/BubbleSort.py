#Dicas do Professor: Desenhar, ilustrar para visualizar e conseguir compreender da melhor forma possível sempre!!!


def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
