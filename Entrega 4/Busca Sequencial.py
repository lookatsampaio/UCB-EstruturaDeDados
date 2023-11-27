def linearSearch(prateleiras, posicaoPrateleira, medicamentoProcurado):
    for i in range (0, posicaoPrateleira):   #Lê os medicamento sequencialmente
        if (prateleiras[i] == medicamentoProcurado):
            return i
    return -1

#Código Principal
#
prateleiras = ['B-Suprin', 'Gaballon', 'Halo','Kaletra','Labcaína Geleia 2%','AmomedicamentoProcuradoicilina','NEOPet']
medicamentoProcurado = "NEOPet"
posicaoPrateleira = len(prateleiras)
result = linearSearch(prateleiras, posicaoPrateleira, medicamentoProcurado)
if(result == -1):
    print("Medicamento não encontrado")
else:
    print("Medicamento na prateleira:", result)