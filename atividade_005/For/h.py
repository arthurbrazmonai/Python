# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 23/05/2024
# Atividade 005 - H


import os


os.system('cls')

inicial = int(input('Insira um numero inicial: '))
final = int(input('Insira um numero final: '))

ignorar1 = int(input('Insira um numere para ignorar: '))
ignorar2 = int(input('Insira um numere para ignorar: '))
ignorar3 = int(input('Insira um numere para ignorar: '))

for c in range(inicial, (final + 1)):
    if ((c == ignorar1) or (c == ignorar2) or (c == ignorar3)):
        continue
    print(c, end='|')