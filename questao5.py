def menu():
    op = int(input("Digite 1 para inserir item na pilha e 2 para visualizar a pilha e 0 para sair: "))
    return op


def __main__():
    tarefas=[]
    op = menu()
    while op != 0:
        if op == 1:
            inserirPilha(tarefas)
        elif op == 2:
            print(retornarUltimaTarefa(tarefas))
        op = menu()

def inserirPilha(tarefas):
    tarefa = input ("Digite a tarefa para inserir na pilha: ")
    tarefas.append(tarefa)
    return tarefas

def retornarUltimaTarefa(tarefas):
    return tarefas[-1]

__main__()