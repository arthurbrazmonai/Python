# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 15/05/2024
# Atividade G

# Biblioteca

import os
import math

# Terminal

os.system('cls')

# Receber 

a = int (input('Informe o valor da letra A: '))
b = int (input('Informe o valor da letra B: '))
c = int (input('Informe o valor da letra C: '))

# Processo 

delta = math.pow(b, 2) - (4 * a * c)

re1 = (-b + (math.sqrt(delta))) / (2 * a)
re2 = (-b - (math.sqrt(delta))) / (2 * a)
    
# Condicional 

if delta <0:
    verificacao = 'Erro, o delta deu um numero negativo'
else:
    verificacao = f'As raizes da equaçao e : x1:{re1} e x2:{re2}'

print(verificacao)