import random


def ordenar_pilha(pilha):
    pilha_temporaria = []

    while pilha:
        atual = pilha.pop()
        while pilha_temporaria and pilha_temporaria[-1] > atual:
            pilha.append(pilha_temporaria.pop())
        pilha_temporaria.append(atual)

    while pilha_temporaria:
        pilha.append(pilha_temporaria.pop())

    return pilha


if __name__ == "__main__":
    notas = [random.randint(0, 10) for _ in range(20)]

    print("Notas originais (topo da pilha à esquerda):", notas)
    notas_ordenadas = ordenar_pilha(notas)
    print("Notas ordenadas (topo da pilha à esquerda):", notas_ordenadas)
