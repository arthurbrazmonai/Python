import os 


os.system('cls')

quantidade_impares = 0
soma_impares = 0

for num in range(1, 101, 2):
    quantidade_impares += 1 
    soma_impares += num 

print("Quantidade de números ímpares:", quantidade_impares)
print("Soma dos números ímpares:", soma_impares)
