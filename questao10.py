class Fila:
    def __init__(self, tamanho_maximo=80):
        self.tamanho_maximo = tamanho_maximo
        self.itens = [None] * tamanho_maximo
        self.frente = 0
        self.traseira = -1
        self.tamanho = 0

    def is_empty(self):
        return self.tamanho == 0

    def is_full(self):
        return self.tamanho == self.tamanho_maximo

    def enqueue(self, item):
        if self.is_full():
            print("Erro: A fila está cheia")
            return
        self.traseira = (self.traseira + 1) % self.tamanho_maximo
        self.itens[self.traseira] = item
        self.tamanho += 1

    def dequeue(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        item = self.itens[self.frente]
        self.itens[self.frente] = None
        self.frente = (self.frente + 1) % self.tamanho_maximo
        self.tamanho -= 1
        return item

    def size(self):
        return self.tamanho

    def display(self):
        if self.is_empty():
            print("Fila está vazia")
        else:
            print("Fila:", end=" ")
            for i in range(self.tamanho):
                index = (self.frente + i) % self.tamanho_maximo
                print(self.itens[index], end=" ")
            print()

def inserirCodigos(fila):
    for i in range(80):
        fila.enqueue(i + 3)

def contarImpares(fila):
    cont = 0
    for i in range(fila.size()):
        index = (fila.frente + i) % fila.tamanho_maximo
        if fila.itens[index] % 2 != 0:
            cont += 1
    return cont

def __main__():
    livros = Fila()
    inserirCodigos(livros)
    livros.display()
    print("Números ímpares:", contarImpares(livros))

__main__()
