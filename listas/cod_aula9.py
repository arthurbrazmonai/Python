import os


os.system('cls')

entrada = input('Digite numeros separados por espaço: ')

numeros_str = entrada.split()

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
print('lista fornecida:', numeros)

escolha = input('Deseja inverter a ordem da lista? (s/n): ').strip().lower()

if escolha == 's':
    numeros.reverse()
    print('Lista invertida:', numeros)
else:
    print('A lista nao foi invertida')