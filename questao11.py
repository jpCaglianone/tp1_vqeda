class Pilha:
    def __init__(self, tamanho_maximo=10):
        self.tamanho_maximo = tamanho_maximo
        self.itens = [None] * tamanho_maximo
        self.topo = -1

    def is_empty(self):
        return self.topo == -1

    def is_full(self):
        return self.topo == self.tamanho_maximo - 1

    def push(self, item):
        if self.is_full():
            print("Erro: A pilha está cheia")
            return
        self.topo += 1
        self.itens[self.topo] = item

    def pop(self):
        if self.is_empty():
            print("Erro: A pilha está vazia")
            return None
        item = self.itens[self.topo]
        self.itens[self.topo] = None
        self.topo -= 1
        return item

    def size(self):
        return self.topo + 1


def menu ():
    op = int(input("Digite 1 para adicionar alguem a fila, digite 2 para atender alguem , digite 3 para ver o tamanho da fila e 0 para sair"))
    return op


def __main__():
    fila
    op = menu()
    while op != 0:
        if op == 1:
            nome = input("Insira o nome que deseja adicionar: ")

