# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 26/04/2024

# Biblioteca

import os

# Terminal

os.system ('cls')

print ('='* 70)
print ('EXERCICIO DE CONDICIONAL: H')
print ('='* 70)

# Entrada

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)

print (f'x1 = {x1}')
print (f'x2 = {x2}')
