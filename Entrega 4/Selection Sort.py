def selectionSort(array, size):
    for etapa in range(size):
        valor_min = etapa

        for i in range(etapa + 1, size):
            if array[i] < array[valor_min]:        # seleciona o valor minimo encontrado em cada loop
                valor_min = i
        (array[etapa], array[valor_min]) = (array[valor_min], array[etapa]) # coloca o valor minimo na posição correta


Medicamentos = ['Gaballon','Amoxicilina', 'Kaletra', 'Labcaína Geleia 2%', 'Halo']
size = len(Medicamentos)
print("Lista atual:\n",Medicamentos) #Lista os Medicamentos como são inseridos
selectionSort(Medicamentos, size) #realiza a organização através do Selection Sort
print("\n\Lista organizada:\n", Medicamentos) #Lista os Medicamentos já organizados pela Selection sort