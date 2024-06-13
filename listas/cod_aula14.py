import os


os.system('cls')

soma = 0

lista_mumeros = [1,2,3,4,5,6,7,8,9,10]

if (3 in lista_mumeros):
    print(lista_mumeros)
    posicao =lista_mumeros.index(3)
    print(f'O numero 3 esta na posiçao {posicao}')
else:
    print('O elemento nao constam na listagem')
    
lista_nomes = ['jhon','jane','carol']

if( 'maria' not in lista_nomes):

    lista_nomes.append('maria')

print('\n O nome Maria foi acrescentadio')
print(lista_nomes)