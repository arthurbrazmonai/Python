import os 


os.system('cls')

lista = [1,2,3,4]

posicao = int(input('inisra a numeraçao da posiçao: '))
elemento = input('Insira os elementos:')

if posicao >= 0 and posicao <= len(lista):
    lista.insert(posicao,elemento)
    print(f'Lista apos inserçao', lista)
else:
    print(f'Posiçao fora do intervalo,{len(lista)}')