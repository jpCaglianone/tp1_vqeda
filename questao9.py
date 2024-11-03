def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                # Troca os elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def __main__():
    numeros = [64, 34, 25, 12, 22, 11, 90, 103, 2, 2905, 1, 34]

    print("Lista original:", numeros)
    numeros_ordenados = ordenar_lista(numeros)
    print("Lista ordenada:", numeros_ordenados)

__main__()