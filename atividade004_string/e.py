import os

os.system('cls')

frase = input('Insira uma frase: ')

if frase in 'a' or 'e' or 'i' or 'o' or 'u':
   a = frase.count('a')
   e = frase.count('e')
   i = frase.count('i')
   o = frase.count('o')
   u = frase.count('u')
   print(f'{a} a, {e} e, {i} i, {o} o, {u} u,')
else:
    print('Nao a vogais')