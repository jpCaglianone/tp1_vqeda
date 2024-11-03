class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def is_empty(self):
        return self.tamanho == 0

    def is_full(self):
        return self.tamanho == self.capacidade

    def enqueue(self, item):
        if self.is_full():
            print("Erro: A fila está cheia")
            return
        self.itens[self.fim] = item
        self.fim += 1
        self.tamanho += 1
        if self.fim == self.capacidade:
            self.fim = 0

    def dequeue(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        item = self.itens[self.inicio]
        self.itens[self.inicio] = None
        self.inicio += 1
        self.tamanho -= 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        return item

    def size(self):
        return self.tamanho


def menu ():
    op = int(input("Digite 1 para adicionar alguem a fila, digite 2 para atender alguem , digite 3 para ver o tamanho da fila e 0 para sair: "))
    return op


def __main__():
    fila = Fila(100)
    op = menu()
    while op != 0:
        if op == 1:
            nome = input("Insira o nome que deseja adicionar: ")
            fila.enqueue(nome)
        if op == 2:
            print(f"Senhor(a) {fila.itens[fila.inicio]}, favor encaminhe-se para ser atendido!")
            fila.dequeue()
        if op == 3:
            print(f"Ainda ha {fila.size()} pessoa(s) na fila")

        op = menu()

__main__()
