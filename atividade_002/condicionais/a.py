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

numero = input ('Insira o numero: ')
resposta = ''

# Condicional 

if numero % 2 == 0:
    resposta = f'O numero {numero} e par'
else:
    resposta = f'O numero {numero} e impar'

# Saida 

print (resposta)

print ('fim do programa!\n')
