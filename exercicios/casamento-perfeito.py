"""
Dado um texto de entrada, você deverá escrever um programa em python 3 que verificará se há um casamento perfeito entre os parênteses, colchetes e chaves em uma string. Um casamento perfeito ocorre quando os delimitadores da string (parênteses, colchetes e chaves) à esquerda possuem os correspondentes à direita na ordem de ocorrência inversa, tal como utilizado nas equações matemáticas.

REGRA GERAL: você deverá usar uma pilha para armazenar os delimitadores que forem abertos e ela deve ser a única estrutura de armazenamento de dados utilizada no algoritmo. Não é permitido usar bibliotecas. É permitido o uso de uma lista de python e somente as funções da lista: len, append e pop para armazenar a pilha.
"""

def casamento_perfeito(texto):
    pilha = [] # A pilha será utilizada para armazenar os delimitadores abertos
    
    for char in texto: # percorre cada caractere na string
        if char in '([{': # se for um delimitador de abertura
            pilha.append(char)
        elif char in ')]}': # se for um delimitador de fechamento
            if len(pilha) == 0: # verifica se a pilha está vazia ou se o topo da pilha não corresponde
                return False
            topo = pilha.pop() # Retira o topo da pilha para verificar o casamento
            # Verifica se o topo da pilha corresponde ao delimitador de fechamento atual (iterável char)
            if char == ')' and topo != '(':
                return False
            elif char == ']' and topo != '[':
                return False
            elif char == '}' and topo != '{':
                return False
    
    return len(pilha) == 0 # No final, a pilha deve estar vazia para um casamento perfeito. Ou seja, retorna True se a pilha estiver vazia, caso contrário, retorna False.

texto = input("")
if casamento_perfeito(texto):
    print("casamento perfeito")
else:
    print("casamento imperfeito")