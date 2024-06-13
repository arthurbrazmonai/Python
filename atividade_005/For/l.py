import os 


os.system('cls')

banco_nomes = 'arthur layza luiza marcelo'
banco_senhas = '1234567 b7654321 c6547890' 



usuario = input ('Insira o nome do usuario: ')
senha = input('Insira a senha: ')

if usuario in banco_nomes and senha in banco_senhas:
    print ('achou')