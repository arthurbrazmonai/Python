import os


os.system('cls')

lista_numeros = []

entrada = input('Digite um numero: ')

numeros = entrada.split()

pares = []

for numero in numeros:
    
    numero_aux = int(numero)
    
    if   numero_aux % 2 == 0:
        pares.append( numero_aux)
        
lista_numeros.extend(pares)

print(f'Numeros pares adicionado na lista: {lista_numeros}')