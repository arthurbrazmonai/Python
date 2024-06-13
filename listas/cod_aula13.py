import os


os.system('cls')

soma = 0

lista_mumeros = [1,2,3,4,5,6,7,8,9,10]

for indice, numero in enumerate(lista_mumeros):
    soma += numero
    print(f'Indice: {indice} = Numero: {numero}')