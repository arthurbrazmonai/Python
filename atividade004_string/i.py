# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 23/05/2024
# Calculo de Perimeto

import os

os.system('cls')

nome = input('Insira seu nome completo: ')

if nome.isdigit():
    print('Erro!!!')
else:
    separar_nome = nome.split(' ')
    pri_nome = f'{separar_nome[0]}'
    sobrenome = f'{separar_nome[-1]}'
    print (f'Nome: {pri_nome}, Sobrenome: {sobrenome}')
