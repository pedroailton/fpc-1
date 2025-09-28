def buscaBinaria(elemento, lista, qtd_comparacoes=0):
    if len(lista) == 0: # Caso base: Lista vazia (não faz mais comparações)
        return qtd_comparacoes
    else:
        meio = len(lista)//2
        if lista[meio] == elemento:
            qtd_comparacoes += 1
            return qtd_comparacoes
        elif lista[meio] < elemento: # O elemento está à direita
            qtd_comparacoes += 1
            return buscaBinaria(elemento, lista[meio+1:], qtd_comparacoes)
        elif lista[meio] > elemento: # O elemento está à esquerda
            qtd_comparacoes += 1
            return buscaBinaria(elemento, lista[:meio], qtd_comparacoes)

elemento = 0
lista = []
resultado = 0

entrada = input("").strip()
elementos_da_entrada = entrada.split(" ")

for i in elementos_da_entrada:
    lista.append(int(i))

elemento = lista[0]
lista = lista[1:]

resultado = buscaBinaria(elemento, lista)
print(resultado)