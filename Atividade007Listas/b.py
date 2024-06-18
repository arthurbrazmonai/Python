# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 17/06/2024
# Atividade 007: Listas

import os
import random

lista = []
numero = 0

for i in range (1,50):
    numero = random.randint(0,100)

    lista.append(int(numero))

for i in range (1,10):
    print (lista)
    print ()
