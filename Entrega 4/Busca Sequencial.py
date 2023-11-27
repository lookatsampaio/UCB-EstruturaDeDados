def linearSearch(prateleiras, posicaoPrateleira, medicamentoProcurado):
    for i in range (0, posicaoPrateleira):   #Lê os medicamento sequencialmente
        if (prateleiras[i] == medicamentoProcurado):
            return i
    return -1

#Código Principal
#Lista medicamentos por prateleira
prateleiras = ['B-Suprin', 'Gaballon', 'Halo','Kaletra','Labcaína Geleia 2%','AmomedicamentoProcuradoicilina','NEOPet']
medicamentoProcurado = "Halo" #Medicamento procurado
posicaoPrateleira = len(prateleiras) #define o tamanho da prateleira
prateleiraMedicamento = linearSearch(prateleiras, posicaoPrateleira, medicamentoProcurado)
if(prateleiraMedicamento == -1):
    print("Medicamento não encontrado") #Medicamento caso não encontrado, quando a função resulta em "0"
else:
    print("Medicamento na prateleira:", prateleiraMedicamento) #Medicamento encotrado e informa a prateleira em que se encontra