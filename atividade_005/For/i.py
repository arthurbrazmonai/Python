# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 23/05/2024
# Atividade 005 - H


import os
import time

os.system('cls')

while True:
    print('Estou em looping')
    time.sleep(2)
    print()
    parada = input('Deseja finalizar p programa [f - sim]?').lower()
    
    if parada == 'f':
        break