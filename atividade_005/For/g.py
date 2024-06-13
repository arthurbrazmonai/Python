# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 23/05/2024
# Atividade 005 - G


import os


os.system('cls')

primo1  = int(input('Insira um numero negativo: '))
primo2  = int(input('Insira um numero negativo: '))

if primo1 < 2:
    print('Erro !!!')
    
for c in range(primo1, (primo2 + 1)):
        for i in range(primo1,c):
            if c % 1 == 0:
                break
        else:
            print(c, end='|')