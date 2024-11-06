class TabelaHash:
    def __init__(self, tamanho):
        self.tabela = [[] for _ in range(tamanho)]
        self.tamanho = tamanho

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        for i, item in enumerate(self.tabela[indice]):
            if item[0] == chave:
                del self.tabela[indice][i]
                return True
        return False


tabela = TabelaHash(10)

tabela.inserir("chave1", "valor1")
tabela.inserir("chave2", "valor2")
tabela.inserir("chave3", "valor3")
tabela.inserir("chave4", "valor4")

print(tabela.buscar("chave1"))  # valor1
print(tabela.buscar("chave2"))  # valor2
print(tabela.buscar("chave3"))  # valor3

tabela.remover("chave2")
print(tabela.buscar("chave2"))  # None

tabela.inserir("chave3", "novo_valor3")
print(tabela.buscar("chave3"))  # novo_valor3

print(tabela.buscar("chave5"))  # None
