from math import floor

def buscaBinaria(elemento, lista, qtd_comparacoes=0):
    if len(lista) == 0: # Caso base: Lista vazia (não faz mais comparações)
        return qtd_comparacoes
    else:
        if len(lista) % 2 == 0: # Se o tamanho da lista for par
            meio = len(lista)/2
        else: # Se o tamanho da lista for ímpar
            meio = floor(len(lista)/2)
        if meio == elemento:
            qtd_comparacoes += 1
            return qtd_comparacoes
        elif meio < elemento: # O elemento está à direita
            qtd_comparacoes += 1
            return buscaBinaria(elemento, lista[meio+1:], qtd_comparacoes)
        elif meio > elemento: # O elemento está à esquerda
            qtd_comparacoes += 1
            return buscaBinaria(elemento, lista[0:meio-1], qtd_comparacoes)

elemento = 0
lista = []
resultado = 0

entrada = input("")
elementos_da_entrada = entrada.split(" ")

for i in elementos_da_entrada:
    lista.append(int(i))

elemento = lista[0]
lista = lista[1:]

resultado = buscaBinaria(elemento, lista)
print(resultado)