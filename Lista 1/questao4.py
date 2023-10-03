# Manipulação de arquivos
arquivo = open('/lista2509/teste1.txt', 'r+')
def adicionando():
  print("======ADICIONAR=====")
  arquivo.write('Estou no arquivo teste1.txt\n')
  texto_longo = "Coming home is terrible\nwhether the dogs lick your face or not;\nwhether you have a wife,\nor just a wife-shaped loneliness waiting for you."
  arquivo.write(texto_longo)
  arquivo.seek(0)
  conteudo = arquivo.read()
  print(conteudo)
  arquivo.close()

# É importante fechar o arquivo depois de terminar de
#escrever para liberar os recursos do sistema operacional.


def listando():
   print("======LISTAR=======")
   arquivo = open('/lista2509/teste1.txt','r')
   conteudo = arquivo.read()
   print(conteudo)
   arquivo.close()

def alterando():
    print("=======ALTERAR======")

    with open('/lista2509/teste1.txt', 'r+') as arquivo:
        texto_longo = "Coming home is terrible\nwhether the dogs lick your face or not;\nwhether you have a wife,\nor just a wife-shaped loneliness waiting for you."
        
        arquivo.write(texto_longo)
        
    with open('/lista2509/teste1.txt', 'w') as arquivo:
        texto_curto = "Everything you see now,\nall of it: bone."
        arquivo.write(texto_curto)
    with open('/lista2509/teste1.txt', 'r') as arquivo:
      print(arquivo.read())

def deletando():
  print("======DELETAR======")
  with open('/lista2509/teste1.txt', 'r') as arquivo:
    print("ANTES DE APAGAR O CONTEUDO")
    print(arquivo.read())
  with open('/lista2509/teste1.txt', 'w') as arquivo:
    print("DEPOIS DE APAGAR O CONTEUDO")
    arquivo.write("todo conteudo anteiror foi apagado e essa string foi adicionada")
  with open('/lista2509/teste1.txt', 'r') as arquivo:
      print(arquivo.read())
# MANIPULANDO O ARQUIVO /lista2509/teste1.txt
# 1
adicionando()
# 2
listando()
# 3
alterando()
# 4
deletando()