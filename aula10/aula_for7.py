import os

os.system('cls')

while (True):
    
    nome = str(input('Digite um nome [s _ sair]')).lower()
    
    if (nome != 's'):
        print('Continue digitando...')
    else:
        print('Voce digitou "s" para sair!')
        
        break