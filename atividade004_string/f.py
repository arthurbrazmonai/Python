import os 

os.system('cls')

nome_completo = 'anderson,silva'

if nome_completo.isdigit():
    print(nome_completo.split(','))
else:
    print('Invalido!!!')