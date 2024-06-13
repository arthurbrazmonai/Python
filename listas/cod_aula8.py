import os


os.system('cls')

entrada = input('Digite numeros separados por espaço: ')

numeros_str = entrada.split()

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
ordem = input ("Digite 'asc' para ordem ascendente ou 'desc'"
+ "para ordem descendente: ").strip().lower()

if ordem == 'asc':
    numeros.sort()
    print(f'Lista ordenada em ordem ascendente: {numeros}')
elif ordem == 'desc':
    numeros.sort(reverse=True)
    print(f'Lista ordenada em ordem descendente: {numeros}')
