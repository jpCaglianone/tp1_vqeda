import random


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    lista_esquerda = merge_sort(lista[:meio])
    lista_direita = merge_sort(lista[meio:])

    return merge(lista_esquerda, lista_direita)


def merge(lista_esquerda, lista_direita):
    lista_resultante = []
    i = 0
    j = 0

    while i < len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i] < lista_direita[j]:
            lista_resultante.append(lista_esquerda[i])
            i += 1
        else:
            lista_resultante.append(lista_direita[j])
            j += 1

    lista_resultante.extend(lista_esquerda[i:])
    lista_resultante.extend(lista_direita[j:])

    return lista_resultante


lista = [random.randint(1, 500000) for _ in range(500000)]
print(f"-------------------- Lista não ordenada ----------------------- \n{lista}")
lista_ordenada = merge_sort(lista)
print(f"-------------------- Lista ordenada ----------------------- \n{lista_ordenada}")
