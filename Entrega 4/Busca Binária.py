def buscaBinaria(array, x, low, high):
    while low <= high: #repete até que o indicadores maior e o menor se encontrem
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Código principal
array = ['B-Suprin',  'Gaballon', 'Halo','Kaletra','Labcaína Geleia 2%','Amoxicilina']
x = "Gaballon"
result = buscaBinaria(array, x, 0, len(array)-1)
if result != -1:
    print("Medicamento na prateleira:  ")
    print(result+1)
else:
    print("Medicamento não encontrado")