paises = []

def criar_pais():
    nome = input("Digite o nome do pais que deseja adicionar: ")
    paises.append(nome)
    print(f"Pais '{nome}' adicionado com sucesso!")

def ler_paises():
    if not paises:
        print("Lista vazia")
    else:
        print("Lista de paises:")
        for i, pais in enumerate(paises, 1):
            print(f"{i}. {pais}")

def atualizar_pais():
    ler_paises()
    indice = int(input("Digite o numero do pais que deseja alterar: ")) - 1

    if indice < 0 or indice >= len(paises):
        print("Indice invalido. Tente novamente.")
    else:
        novo_nome = input(f"Digite o novo nome para '{paises[indice]}': ")
        paises[indice] = novo_nome
        print(f"Pais '{novo_nome}' atualizado!")

def excluir_pais():
    ler_paises()
    indice = int(input("Digite o numero do pais que deseja excluir: ")) - 1

    if indice < 0 or indice >= len(paises):
        print("Indice invalido. Tente novamente.")
    else:
        pais_excluido = paises.pop(indice)
        print(f"Pais '{pais_excluido}' excluido!")


#Menu
while True:                                 
    print("\nMENU")
    print("1. Adicionar país")
    print("2. Listar países")
    print("3. Atualizar país")
    print("4. Excluir país")
    print("5. Fechar programa\n")

    opcao = input("Digite o que deseja fazer: ")

    if   opcao == "1":
        criar_pais()
    elif opcao == "2":
        ler_paises()
    elif opcao == "3":
        atualizar_pais()
    elif opcao == "4":
        excluir_pais()
    elif opcao == "5":
        print("Progama finalizado\n\n\n")
        break
    else:
        print("Opcao invalida")
