# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

# Biblioteca

import os

# Terminal

os.system ('cls')

print ('='* 70)
print ('ESTUDO DE CONDICIONAL: PARTE 1')
print ('='* 70)

# Entrada 

numero1 = int (input ('Insira o numero1: '))
numero2 = int (input ('Insira o numero2: '))
numero3 = int (input ('Insira o numero3: '))

# Condicional

if numero1 > numero2 and numero1 > numero3:
    
    print (f'{numero1} e maior')


if numero2 > numero1 and numero2 > numero3:
    
    print (f'{numero2} e maior')
    
if numero3 > numero1 and numero3 > numero2:
    
    print (f'{numero1} e maior')
     
     
    
    
    