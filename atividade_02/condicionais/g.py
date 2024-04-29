# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 26/04/2024

# Biblioteca

import os

# Terminal

os.system ('cls')

print ('='* 70)
print ('EXERCICIO DE CONDICIONAL: G')
print ('='* 70)

# Entrada

a = input ('insira o valor 1: ')
b = input ('insira o valor 2: ')
c= input ('insira o valor 3: ')

# Condicionais

if (a + b > c and  b + c > a and c + a > b) :
    
 print ( 'Pode ser um triangulo')
else:
 print ( 'Nao pode ser um triangulo')