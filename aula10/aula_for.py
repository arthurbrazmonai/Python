import os

os.system('cls')

soma = 0

for var_inte in range (0,4):
    numero = int(input(f'{var_inte + 1}º numero: '))
    
    if (numero % 2 == 0):
        print(f'O numero {numero} e par')
    else:
        print(f'O numero {numero} e impar')
    