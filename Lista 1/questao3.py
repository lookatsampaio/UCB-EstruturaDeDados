def atualizar_jogador(entrada, indice, novo_nome):
    if entrada[0] == indice:
        return (indice, novo_nome)
    else:
        return entrada


colecao_jogadores = []
limite = 20

nome_jogador = input(f"Digite o nome do jogador {len(colecao_jogadores) + 1}: ")
colecao_jogadores.append((len(colecao_jogadores), nome_jogador))

while len(colecao_jogadores) < limite:
  ad =  input("Quer colocar mais um jogador? (s ou n):")
  if ad == 's':
     nome_jogador = input(f"Digite o nome do jogador {len(colecao_jogadores) + 1}: ")
     colecao_jogadores.append((len(colecao_jogadores), nome_jogador))
  else: 
     break

print("Coleção de jogadores:")
print(colecao_jogadores)

print("========UPDATE=======")
indice = int(input("Digite o índice do jogador a ser substituído: "))


if 0 <= indice < len(colecao_jogadores):
    novo_nome = input("Digite o novo nome do jogador: ")
    colecao_modificada = list(map(lambda x: atualizar_jogador(x, indice, novo_nome), colecao_jogadores))
    print("Coleção de jogadores atualizada:")
    print(colecao_modificada)
else:
    print("Índice inválido. Nenhum jogador foi modificado.")
    print()
print("=======DELETE======")


def apagando(indice,colecao_jogadores):
    if 0 <= indice < len(colecao_modificada):
        del colecao_modificada[indice]
    else:
        print("Índice inválido. Nenhum jogador foi deletado.")
    return colecao_modificada


try:
    indice = int(input("Digite o índice do jogador a ser deletado: "))
except ValueError:
    print("Entrada inválida. Digite um número inteiro para o índice.")

colecao_modificada = list(map(apagando, [indice], [colecao_modificada]))
print("Coleção de jogadores atualizada:")
print(colecao_modificada)


print("========READ========")
def lendo_colecao(colecao_modificada,resposta):
  if resposta == 's':
   print(colecao_modificada)


resposta = input('Quer ler sua colecao(digite s ou n): ')


colecao_modificada = list(map(lendo_colecao,[colecao_modificada],[resposta]))


print("=========CREATE=========")
nome_colecao = input("Dê um nome para sua nova colecao de jogadores: ")

def criando_colecao(i):
    return input(f"Adicione o nome do jogador {i+1} à sua lista: ")

# Use map para criar uma lista de jogadores
nova_colecao = list(map(criando_colecao, range(5)))

print("Nova coleção de jogadores:")
print(nova_colecao)