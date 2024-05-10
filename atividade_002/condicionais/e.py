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

# variavel

resultado = 0

# Entrada 

rodar = float (input ('Insira quantidade de KM: '))

# Condicionais

if rodar <= 200:
    resultado = 0.70 * rodar
else:
    resultado = 0.40 * rodar
    
print (f'O preço sera de {resultado} reais')