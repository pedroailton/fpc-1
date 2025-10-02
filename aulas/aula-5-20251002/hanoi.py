# Definindo as hastes
A = []
B = []
C = []

def hanoi2(origem, destino, auxiliar):
    elem = origem.pop() # Disco n1
    auxiliar.append(elem)
    print('Movimentando disco da ')

    elem = origem.pop() # Disco n2
    destino.append(elem)

    elem = auxiliar.pop() # Disco n1
    destino.append(elem)

    return destino

def hanoi3(origem="A", destino="C", auxiliar="B"):
    hanoi2(origem, auxiliar, destino)
    print(f"Movimentando o disco 3 da pilha {origem} para {destino}")
    hanoi2(auxiliar, destino, origem)