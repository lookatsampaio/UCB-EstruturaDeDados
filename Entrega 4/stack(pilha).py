# Creating a pilha
def create_stack():
    pilha = []
    return pilha
# Creating an empty pilha
def check_empty(pilha):
    return len(pilha) == 0
# Adding items into the pilha
def push(pilha, item):
    pilha.append(item)
    print("pushed item: " + item)
# Removing an element from the pilha
def pop(pilha):
    if (check_empty(pilha)):
        return "pilha is empty"

    return pilha.pop()


pilha = create_stack()
push(pilha, str(1))
push(pilha, str(2))
push(pilha, str(3))
push(pilha, str(4))
push(pilha, str(8))
push(pilha, str(4))
print("popped item: " + pop(pilha))
print("pilha after popping an element: " + str(pilha))