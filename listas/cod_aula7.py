import os


os.system('cls')

entrada = input('Digite numeros separados por espaço: ')

numeros_str = entrada.split()

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
busca_numero = int(input('Digite o numero que deseja encontrar: '))

if busca_numero.index(busca_numero):
    indice = numeros.index(busca_numero)
    print(f'O numero {busca_numero} esta no indice {indice}.')
else:
    print(f'O numero {busca_numero} nao foi encontrado na lista.')
    
print(f'Lista fornecido: {numeros}')