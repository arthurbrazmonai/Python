# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

import os 

os.system('cls')

numero = input('Insira um numero: ')
stingq = len(numero)
valida = False

if numero.isdigit() and stingq > 0 and stingq <= 4 :
    print("Número válido!")
    valida = True
else:
    print("Número inválido!")
 
print('-'*70)
    
if stingq > 0 and valida == True:
    print(f'{numero[3:4]} unidade')

if stingq > 1 and valida == True:
    print(f'{numero[2:3]} dezena')

if stingq > 2 and valida == True:
    print(f'{numero[1:2]} centena')

if stingq > 3 and valida == True:
    print(f'{numero[0:1]} unidade de milhar')