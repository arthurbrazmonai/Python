# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

import os 

os.system('cls')

# Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 'o' aparece e em que posição ela aparece pela primeira e última vez.

nome = input('Insira seu nome: ')
validado = False

if nome.isdigit():
    validado = False
else:
    validado == True

if validado == True:
    quantidade = nome.count('o')



print(quantidade)