# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 15/05/2024
# Atividade F

# Biblioteca

import os
import random

# Terminal

os.system('cls')

# Receber 

numero = int (input('Escreva um numero entre 1 a 10: '))

# Processammento

numero_aleatorio = random.radint(1,10)

# Condicional

if numero < 1 or numero > 10:
    mensagem1 = 'O numero nao esta entre 1 e 10'
else:
    mensagem1 = 'Numero aceito'
    
if numero == numero_aleatorio:
    resposta = f'Parabens voce acertou, o numero {numero_aleatorio}'
else:
    resposta = f'Que pena voce errou, o numero certo e {numero_aleatorio}'
    
print (resposta) 