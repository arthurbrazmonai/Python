# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 23/05/2024
# Calculo de Perimeto

import os 

os.system('cls')

nome = input('Insira seu nome: ')

if nome.isdigit():
    print('Erro!!!')
else:
    quant_o = nome.count('o')
    primeiro_o = nome.find('o') + 1
    ultimo_o = nome.rfind('o') + 1
    print( f'O nome tem {quant_o} o,' 
    +f'O primeiro o esta na posiçao: {primeiro_o},' 
    +f'O ultimo o esta na posiçao: {ultimo_o}')