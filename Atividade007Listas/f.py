# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 17/06/2024
# Atividade 007: Listas

import os
import random

os.system('cls')

numero = 0
num_lista = []

lista_c = []
lista_d = []

for numero in range(1,10):
    numero = random.randint(0,100)
    num_lista.append(numero)

lista_c = num_lista.sort()
lista_d = num_lista.sort(reverse=True)
    
print(f'lista crescente: {lista_c}')
print(f'lista decrescente: {lista_d}')
