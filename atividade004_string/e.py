import os

os.system('cls')

frase = input('Insira uma frase: ')

if frase in 'a' or 'e' or 'i' or 'o' or 'u':
   print(len(frase))
else:
    print('Nao a vogais')