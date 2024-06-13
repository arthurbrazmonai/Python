import os


os.system('cls')

lista_mista = ['a', 'b', 3, 'jonh','e',500,'g','h']

lista_fatiada1 = lista_mista[0]
lista_fatiada2 = lista_mista[0:]
lista_fatiada3 = lista_mista[0:6]
lista_fatiada4 = lista_mista[0:6:2]
lista_fatiada5 = lista_mista[-1]

print(f'Fatiando uma lisa: {lista_fatiada1}\n')
print(f'Fatiando uma lisa: {lista_fatiada2}\n')
print(f'Fatiando uma lisa: {lista_fatiada3}\n')
print(f'Fatiando uma lisa: {lista_fatiada4}\n')
print(f'Fatiando uma lisa: {lista_fatiada5}\n')