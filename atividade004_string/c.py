import os

os.system('cls')

nome = input('Insira o nome: ')

if nome in 'Oliveira' and nome.isdigit():
    print('O sobrenome Oliveira esta presente.')
else:
    print('Oliveira nao esta presente.')