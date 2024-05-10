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

velocidade = float (input ('Velocidade do carro: '))

# Condicional

if velocidade <= 60:
    print (f'Velocidade: {velocidade} KM esta no limite')
else:
      print (f'Velocidade: {velocidade} KM ultrapassou os 60 KM')