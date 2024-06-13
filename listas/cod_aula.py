import os


os.system('cls')

lista_numeros_inteiros = [1,2,3,4]
lista_vogais = ['a','e','i','o','u']
lista_nomes = ['arthur','braz','monai']
lista_heterogenica = ['arthur',70,1.80,'-ab']
duas_lista = [[1,2,3,4],['a','e','i','o','u']]

print(f'lista de numeros inteiros: {lista_numeros_inteiros }')
print(f'lista de vogais: {lista_vogais}')
print(f'lista de nomes: {lista_nomes }')
print(f'lista heterogenica: {lista_heterogenica }')
print(f'lista dentro de outra lista: {duas_lista}')

indice0 =lista_numeros_inteiros
indice1 = lista_vogais
indice2 = lista_nomes 
indice3 = lista_heterogenica
indice4 = duas_lista 

print(f'lista de numeros inteiros: {indice0}')
print(f'lista de vogais: {indice1}')
print(f'lista de nomes: {indice2}')
print(f'lista heterogenica: {indice3}')
print(f'lista dentro de outra lista: {indice4}')
