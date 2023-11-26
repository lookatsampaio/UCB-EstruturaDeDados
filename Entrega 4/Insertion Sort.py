def insertionSort(medicamento):
    for etapa in range(1, len(medicamento)):
        chave = medicamento[etapa]
        j = etapa - 1   
        while j >= 0 and chave < medicamento[j]: #compara chave com cada elemento à esquerda até encontrar o menor
            medicamento[j + 1] = medicamento[j]
            j = j - 1
        # Place chave at after the element just smaller than it.
        medicamento[j + 1] = chave # localiza a chave depois do elemento menor
Medicamentos = ['Gaballon','Amoxicilina', 'Kaletra', 'Labcaína Geleia 2%', 'Halo']
print("Lista atual:\n",Medicamentos) #Lista os medicamentos como são inseridos
insertionSort(Medicamentos) #realiza a organização através do Insertion Sort
print("\n\Lista organizada:\n", Medicamentos) #Lista os medicamentos já organizados pela insertion sort