import os

os.system('cls')

soma = 0

for c in range(0, 5):
    
    numero = input('Digite um numero [0-5]: ')
    
    #Validaçao
    if (not (numero.isnumeric())):
        print(f'{numero} Entrada invalida!')
        print()
    else:
        numero = int(numero)
        
    if (numero >= 0 and numero <= 5):
        print(f'{numero} esta dentro do intervalo [0-5]!')
        print()
    else:
        print(f'{numero} Entrada invalida!')