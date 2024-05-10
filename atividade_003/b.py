# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

# Biblioteca

import os
import math

# Terminal

os.system('cls')

# Receber 

valor1 = int (input('Insira o valor 1 para a divisao: '))
valor2 = int (input('Insira o valor 2 para a divisao: '))

# validar

if valor1 or valor2 == 0:
    print (f'Impossivel utilizar os valores {valor1} e {valor2} para divisao')
    
# Processamento

resultado = valor1 / valor2

# condicionais

if resultado == float:
    resultado = math.ceil(resultado)
    
    print()
