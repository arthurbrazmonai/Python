import os

os.system('cls')

texto = 'Ola, Mundo!!!'

print(f'Texto: {texto}')

if 'Mundo' in texto:
    print('A palavra Mundo esta presente na string.')
else:
    print('A palavra Mundo nao esta presente na string.')
    
texto2 = 'Ola, Python!!!'

if 'Mundo' not in texto2:
    print('A palavra Mundo nao esta presente na string.')
else:
    print('A palavra Mundo esta presente na string.')