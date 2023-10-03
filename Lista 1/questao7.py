import os
import sys
produtos = []
with open("usuario.txt",'w') as arquivo:
  arquivo.write("julia.meireles,abc123")
def Listar_todos_produtos(produtos):
  for produto in produtos:
    print(produto)

def Cadastrar_novo_produto(produtos):
  id = len(produtos) + 1

  descricao = input("Informe a descricao do produto:")
  peso = input("Informe o peso do produto: ")
  valor = input("Informe o valor do produto: ")
  fornecedor = input("Informe o fornecedor do produto: ")

  novo_produto = {'id': id,'descricao': descricao,'peso': peso,'valor':valor,'fornecedor': fornecedor }
  produtos.append(novo_produto)
  print("Produto cadastrado com sucesso.".upper())

def Listar_produtos_ID(produtos,id):
  for produto in produtos:
    if produto['id'] == id:
      print(produto)

def Listar_produtos_ordenados(produtos,ordenacao):
    if ordenacao == 'A':
        produtos.sort(key=lambda x: x['descricao'])
        print(produtos)
    elif ordenacao == 'Z':
        produtos.sort(key=lambda x: x['descricao'], reverse=True)
        print(produtos)
    else:
        print("Opção de ordenação inválida.")

def editar_produto(produtos, id):
    for produto in produtos:
        if produto['id'] == id:
            descricao = input("Nova descrição (atual: {}): ".format(produto['descricao']))
            peso = input("Novo peso (atual: {}): ".format(produto['peso']))
            valor = input("Novo valor (atual: {}): ".format(produto['valor']))
            fornecedor = input("Novo fornecedor (atual: {}): ".format(produto['fornecedor']))

            produto['descricao'] = descricao if descricao else produto['descricao']
            produto['peso'] = peso if peso else produto['peso']
            produto['valor'] = valor if valor else produto['valor']
            produto['fornecedor'] = fornecedor if fornecedor else produto['fornecedor']

            print("Produto atualizado com sucesso.")
            return

    print("Produto com ID {} não encontrado.".format(id))

def excluir_produto(produtos, id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            print("Produto com ID {} excluído.".format(id))
            return

    print("Produto com ID {} não encontrado.".format(id))

def autenticar_usuario():
  usuario = input("Informe o nome de usuário: ")
  senha = input("Informe a senha: ")

  with open("usuario.txt", "r") as arquivo:
      usuario_arquivo, senha_arquivo = arquivo.read().strip().split(",")

  return usuario == usuario_arquivo and senha == senha_arquivo


def main():
    if not autenticar_usuario():
        print("A autenticação falhou. Encerrando o programa.")
        sys.exit(1)

    produtos = []

    if os.path.exists("produtos.txt"):
        with open("produtos.txt", "r") as arquivo:
            for linha in arquivo:
                id, descricao, peso, valor, fornecedor = linha.strip().split(",")
                produto = {
                    'id': int(id),
                    'descricao': descricao,
                    'peso': peso,
                    'valor': valor,
                    'fornecedor': fornecedor
                }
                produtos.append(produto)


    while True:
      print("======MENU=======")
      print("(1) Listar todos os produtos")
      print("(2) Listar produto pelo ID")
      print("(3) Listar todos os produtos ordenados (A/Z)")
      print("(4) Cadastrar novo produto")
      print("(5) Editar produto")
      print("(6) Excluir produto")
      print("(7) Sair do programa")
      print("==================")

      opcao = input("Escolha uma opção no menu: ")
      if opcao == '1':
        Listar_todos_produtos(produtos)
      elif opcao =='4':
        Cadastrar_novo_produto(produtos)
      elif opcao =='2':
        id = int(input("Informe o ID do produto a ser listado: "))
        Listar_produtos_ID(produtos,id)
      elif opcao == '3':
        ordenacao = input("Ordenar em ordem (A)scendente ou (Z)decendente? ").upper()
        Listar_produtos_ordenados(produtos, ordenacao)
      elif opcao == '5':
        id = int(input("Informe o ID do produto a ser editado: "))
        editar_produto(produtos,id)
      elif opcao == '6':
        id = int(input("Informe o ID do produto a ser excluído: "))
        excluir_produto(produtos,id)
      elif  opcao == '7':
        with open("produtos.txt", "w") as arquivo:
          for produto in produtos:
              arquivo.write("{},{},{},{},{}\n".format(produto['id'], produto['descricao'], produto['peso'], produto['valor'], produto['fornecedor']))
              print("Programa encerrado.")
        break
      else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()