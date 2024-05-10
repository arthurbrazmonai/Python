# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

# Biblioteca

import os
import math

# Terminal

os.system('cls') 

# Entrada 

valor = int (input ('Insira o valor da raiz: '))

# Erro

if valor < 0:
    print (f'Programa nao consegue fazer raiz quadrada do numero {valor}, numero negativo complexo')

# Processamento

raizquadrada = math.sqrt(valor)

# Condicional 

if raizquadrada == float:
    raizquadradad = math.ceil(valor)
    print (f'{raizquadradad}')
else:
    print(f'{raizquadrada}')