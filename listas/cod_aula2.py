import os


os.system('cls')

lista_numeros = []

for i in range(3):
    numero = int(input('Digite um numero: '))
    
    lista_numeros.append(numero)
    
numero_verificar = int(input('Digite um numero: '))

if numero_verificar in lista_numeros:
    print(f'O numero {numero_verificar} esta na lista!')
else:
    print(f'O numero {numero_verificar} nao esta na lista!')