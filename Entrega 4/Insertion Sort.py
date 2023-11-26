def insertionSort(medicamento):
    for etapa in range(1, len(medicamento)):
        key = medicamento[etapa]
        j = etapa - 1
        # Compare key with each element on the left of it until an element smaller than it is found       
        while j >= 0 and key < medicamento[j]:
            medicamento[j + 1] = medicamento[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        medicamento[j + 1] = key
Medicamentos = ['Gaballon','Amoxicilina', 'Kaletra', 'Labcaína Geleia 2%', 'Halo']
print("Lista desorganizada:\n",Medicamentos)
insertionSort(Medicamentos)
print("\n\Lista organizada:\n", Medicamentos)