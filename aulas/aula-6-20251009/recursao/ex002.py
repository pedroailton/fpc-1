def soma_lista_aninhada(lista):
    soma = 0
    for elemento in lista:
        if isinstance(elemento, list):
            soma += soma_lista_aninhada(elemento)
        elif isinstance(elemento, int):
            soma += elemento
    return soma

lista = input("Insira a lista: ")
print(soma_lista_aninhada(lista))