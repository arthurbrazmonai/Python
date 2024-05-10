# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

# Biblioteca

import os
import random

# Terminal

os.system('cls') 



numero_aleatorio = random.random()
print (f'o nuemero gerado foi: {numero_aleatorio}')
print ()
aleatorio_inteiro = random.randint(1, 20)
print (f'o nuemero gerado foi: {aleatorio_inteiro}')
print ()
aleatorio_decimal = random.uniform(1, 10)
print (f'o nuemero gerado foi: {aleatorio_decimal}')
print ()
lista = ['agata', 'coly', 'isis', 'bia']
nome_sorteado = random.choice(lista)
print (f'Lista: {lista}')
print (f'O nome sorteado foi: {nome_sorteado}')
print()
lista2 = ['agata', 'coly', 'isis', 'bia']
print (f'Lista antiga: {lista2}')
print ()
random.shuffle(lista2)
print(f'lista nova: {lista2}')
print ()
numeros = [1, 2, 3, 4, 5, 6, 7]
amostra_aleatoria = random.sample(numeros, 5)
print (f'retorno da amostragem: {amostra_aleatoria}')