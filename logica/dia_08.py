# ESTUDO DE MATRIZES EM PYTHON

# COMO CRIAR UMA MATRIZ?

matriz = [[10, 2], [21, 13], [7, 9]]

# Nesse caso, temos 3 linhas (3 elementos presentes na lista) e 2 colunas (itens dentro de cada lista presente na lista maior)
# Pode ser escrita também como:

matriz2 = [
    [5, 7],
    [9, 18],
    [21, 19]
]

# COMO ACESSAR OS ELEMENTOS DA MATRIZ?

print(matriz[1][0])
print(matriz2[1][1])

# Aqui estamos printando o elemento 21, o 1 representa o 2º elemento da lista e o 0 representa o 1º elemento da lista que está dentro.



# Faremos uma geração de Matriz Aleatória:

import random # biblioteca random - serve pra gerar números aleatórios

matriz_principal = [] # lista vazia que armazena todas as linhas da matriz

lin = int(input('Digite a quantidade de Linhas que você deseja na Matriz: ')) # quantidade de linhas
col = int(input('Digite a quantidade de Colunas que você deseja na Matriz: ')) # quantidade de colunas
# Exemplo:
# lin = 3 -> a matriz terá 3 linhas
# col = 4 -> cada linha terá 4 colunas

for i in range(lin): #laço que percorre as linhas

    linha = [] # cria uma nova linha vazia

    for j in range(col): # laço que controla as colunas da linha 

        numero = random.randint(1, 11) # gere um número inteiro entre 1 e 11
        linha.append(numero) # adiciona o número na linha
    
    matriz_principal.append(linha) # adiciona a linha completa na matriz

print(matriz_principal)