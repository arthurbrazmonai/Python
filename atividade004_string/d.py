import os

os.system('cls')

frase = input('Insira uma frase: ')

if frase.isdigit():
    print(frase.lower())
    print(frase.upper())
    print(len(frase))
else:
    print('Invalido!!!')