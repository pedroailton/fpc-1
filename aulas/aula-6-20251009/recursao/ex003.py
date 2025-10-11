def maiorNivel(lista, nivelInicial = 1):
    maior = nivelInicial

    for elemento in lista:
        if isinstance(elemento, list):
            resultado = maiorNivel(elemento, nivelInicial + 1)
            if resultado > maior:
                maior = resultado

    return maior

lista = input("Insira a lista: ")
print(maiorNivel(lista))