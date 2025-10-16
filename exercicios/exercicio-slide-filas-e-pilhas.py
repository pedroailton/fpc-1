"""
Implemente um programa
que utiliza a estrutura de dados pilha
para ler uma string do teclado e
imprimir a string reversa. OBS: Utilize
as funções push e pop
"""
pilha = []
frase_invertida = "" # string vazia

entrada = input("Insira a frase a ser invertida: ").strip()

# empilhamento
for algarismo in entrada:
    pilha.append(algarismo)

# desempilhamento para frase_invertida
for algarismo in pilha[::-1]: # slicing invertido, inverte a string
    frase_invertida += pilha.pop()

print(frase_invertida)