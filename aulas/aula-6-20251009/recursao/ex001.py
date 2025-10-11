def contaPares(lista):
    total = 0
    for i in lista:
        if isinstance(i, list): # se o elemento for uma lista
            total += contaPares(i)
        elif isinstance(i, int):
            if i % 2 == 0: # se o elemento for par
                total += 1
    return total

lista = input("Insira a lista: ")
print(contaPares(lista))