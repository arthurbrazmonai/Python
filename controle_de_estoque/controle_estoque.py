# CONTROLE DE ESTOQUE

import os
import datetime


os.system('cls')

data = datetime.datetime.now()
data_atual = data.strftime('%d/%m/%Y %H:%M')

# Iniciolizando um dicionario de estoque
estoque = {}

while True:

    print('"'*70)
    print('----------> CONTROLE DE ESTOQUE <----------')
    print('"'*70)

    print()
    print('---------- MENU ----------')
    print()
    print('1 - Adicionar item.')
    print('2 - Remover item.')
    print('3 - Ver estoque.')
    print('4 - Sair.')
    print('--------------------------')
    
    escolhido = input('Escolha uma opção de 1 a 4: ')
    
    os.system('cls')
    
    if escolhido == '1':
        
        os.system('cls')
        
        print('='*70)
        print('Adicionar item')
        print('='*70)
        
        nome_item = input('Digite o nome do item: ')
        quantidade = int(input('Digite a quantidade: '))    
    
        if nome_item in estoque:
            estoque[nome_item] += quantidade
        else:
            estoque[nome_item] = quantidade
            
        os.system('cls')
    
        print(f'Item {nome_item} adicionado / atualizado {data_atual} com sucesso!')
        
    elif escolhido == '2':
        
        os.system('cls')
        
        print('='*70)
        print('Excluir intem')
        print('~'*70)
        nome_item = input('Digite o nome do item a ser removido: ')
        print('~'*70)
        
        if nome_item in estoque:
            quantidade = int(input('Digite a quantidade a ser removida: '))
            
            if quantidade <= estoque[nome_item]:
                del estoque[nome_item]
                print(f'Item {estoque}')
                
        os.system('cls')
            
    elif escolhido == '3':
        
        os.system('cls')
        print('='*70)
        print('Estoque')
        print('='*70)
        print(estoque)
        print('-'*70)
        
        
    elif escolhido == '4':
        
        os.system('cls')
        print('~'*70)
        print('Programa finalizado !!!')
        print('~'*70)
        print('Programa esta finalizado, volte logo!!!')
        break
    