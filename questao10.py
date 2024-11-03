from Tools.scripts.dutree import display


class Pilha:
    def __init__(self, tamanho_maximo=80):

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

    def size(self):
        return self.topo + 1

    def display(self):
        print("Pilha:", self.itens)

def inserirCodigos(pilha):
    for i in range(80):
        pilha.push(i+3)

def contarImpares(pilha):
    cont = 0
    for i in range(pilha.size()):
        if pilha.itens[i] % 2 != 0:
            cont += 1
    return cont

def contarPares(pilha):
    cont = 0
    for i in range(pilha.size()):
        if pilha.itens[i] % 2 != 0:
            cont += 1
    return cont

def __main__():
    livros = Pilha()
    inserirCodigos(livros)
    print(livros.display())
    print(contarImpares(livros))


__main__()