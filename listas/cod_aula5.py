import os 


os.system('cls')

lista_numeros = [10,20,30,40,50,60,70,80,90,100]

indice = int(input('Inisra o indice que deseja remover: '))

if indice <=0 and indice < len(lista_numeros):
    
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido: {elemento_removido}')
else:
    print('indice invalido!')
    
print('Liata apos remoçao:',lista_numeros)