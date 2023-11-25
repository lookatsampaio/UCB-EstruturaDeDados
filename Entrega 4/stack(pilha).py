def criar_pilha():# Criar pilha nomeada carrinho
    carrinho = []
    return carrinho
def ta_vazia(carrinho):# Criar pilha vazia pilha
    return len(carrinho) == 0
def push(carrinho, item): # Adicionar itens na pilha
    carrinho.append(item)
    print("item adicionado: " + item)
def pop(carrinho):# Remover ultimo elemento da pilha
    if (ta_vazia(carrinho)):
        return "pilha ta vazia"

    return carrinho.pop()


carrinho = criar_pilha()
push(carrinho, str('B-Suprin')) 
push(carrinho, str('Gaballon'))
push(carrinho, str('Halo'))
push(carrinho, str('Amoxicilina')) #adiciona os items ao carrinho de compra da farmacia
print("Item retirado: " + pop(carrinho)) #retira o ultimo item e escreve qual item
print("Seu carrinho está com os seguintes produtos: " + str(carrinho)) #apresenta a atual situação do carrinho (da pilha)