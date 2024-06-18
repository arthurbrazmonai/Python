# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 17/06/2024
# Atividade 007: Listas

import os

os.system('cls')

lista = []
lista_par = []
lista_impar = []

for i in range(1,7):
    numero = int (input('Insira um numero: '))
    lista.append(numero)

for numero in lista:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
        
print (f'Numeros par: {lista_par}')    
print (f'Numeros impar: {lista_impar}')