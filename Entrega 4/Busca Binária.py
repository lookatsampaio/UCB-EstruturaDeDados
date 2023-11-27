def buscaBinaria(array, medicamentoProcurado, low, high):
    while low <= high: #repete até que o indicadores maior e o menor se encontrem
        mid = low + (high - low)//2
        if array[mid] == medicamentoProcurado:
            return mid
        elif array[mid] < medicamentoProcurado:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Código principal
array = ['B-Suprin',  'Gaballon', 'Halo','Kaletra','Labcaína Geleia 2%','AmomedicamentoProcuradoicilina'] #lista medicamentos por prateleira
medicamentoProcurado = "Halo"  #define medicamento a ser procurado
result = buscaBinaria(array, medicamentoProcurado, 0, len(array)-1)
if result != -1:
    print("Medicamento na prateleira:  ")
    print(result+1)                         #define a prateleira em que está o medicamento
else:
    print("Medicamento não encontrado")     #caso não tenha o medicamento encontrado, será informado que não há