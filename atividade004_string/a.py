import os

os.system('cls')

nome = input('nome: ')
sobrenome = input('sobrenome: ')

if nome.isdigit():
    print (f'seu nome e: {nome} {sobrenome}')
else:
    print('Invalido!!!')
