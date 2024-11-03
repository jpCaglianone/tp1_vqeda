import random


def procurarDuplicadosForcaBruta(numeros):
    duplicados = []
    n = len(numeros)
    for i in range(n):
        for j in range(i + 1, n):
            if numeros[i] == numeros[j] and numeros[i] not in duplicados:
                duplicados.append(numeros[i])
    return duplicados


def procurandoPorSet(numeros):
    observados = set()
    duplicados = set()

    for num in numeros:
        if num in observados:
            duplicados.add(num)
        else:
            observados.add(num)

    return list(duplicados)


numeros = [random.randint(1, 10) for _ in range(100)]

print(numeros)
print(procurarDuplicadosForcaBruta(numeros))
print(procurandoPorSet(numeros) )