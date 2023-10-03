# O algoritmo de ordenação da bolha (Bubble Sort) é um dos algoritmos de ordenação mais simples, mas não muito eficiente para grandes conjuntos de dados. Ele funciona comparando repetidamente pares de elementos adjacentes e trocando-os se estiverem na ordem errada. O processo é repetido até que nenhuma troca seja necessária, o que indica que a lista está ordenada.
# Aqui está uma implementação básica do algoritmo Bubble Sort em Python:

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Flag para verificar se houve troca em uma passagem
        troca_ocorreu = False

        # Últimos 'i' elementos já estão na posição correta
        for j in range(0, n-i-1):
            # Comparar o elemento atual com o próximo elemento
            if lista[j] > lista[j+1]:
                # Trocar os elementos se estiverem fora de ordem
                lista[j], lista[j+1] = lista[j+1], lista[j]
                troca_ocorreu = True

        # Se nenhuma troca ocorreu durante uma passagem, a lista está ordenada
        if not troca_ocorreu:
            break

# Exemplo de uso:
minha_lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(minha_lista)
print("Lista ordenada:", minha_lista)

# Neste código, o loop externo executa n iterações, onde n é o número de elementos na lista. O loop interno compara pares de elementos adjacentes e os troca se estiverem fora de ordem. Se nenhuma troca ocorrer durante uma passagem completa, isso significa que a lista está ordenada, e o algoritmo para.
# Lembre-se de que o Bubble Sort não é a melhor escolha para grandes conjuntos de dados, pois tem uma complexidade de tempo média de O(n^2), onde 'n' é o número de elementos na lista. Existem algoritmos de ordenação mais eficientes, como Quick Sort, Merge Sort e Tim Sort, que são preferíveis para conjuntos de dados maiores.