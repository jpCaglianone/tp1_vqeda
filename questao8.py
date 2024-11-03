
fila_ordenada =  [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
    "Fernanda", "Gabriel", "Heloísa", "Igor", "Juliana",
    "Karla", "Lucas", "Mariana", "Nicolas", "Olga",
    "Paulo", "Quélia", "Ricardo", "Sofia", "Thiago",
    "Ursula", "Victor", "Wendy", "Xuxa", "Yasmin",
    "Zeca", "Alice", "Beto", "Cecília", "Davi",
    "Eliane", "Fábio", "Gustavo", "Helena"]

def inverterFila(fila):
    fila_invertida = []
    for i in range(len(fila)-1,0,-1):
        fila_invertida.append(fila[i])

    print(fila_invertida)

inverterFila(fila_ordenada)


