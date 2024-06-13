import os 


os.system('cls')

entrada = input('digite numeros separados por espaço: ')

numeros_str = input('digite numeros separados por espaço: ')

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))
    
numero_para_contar = int(input('Digite o numero que deseja contar:'))

contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'O numero {numero_para_contar} aparece {contagem} vezes ma lista.')
else:
    print(f'O numero {numero_para_contar} nao aparece na lista.')
    
print(f'Lista fornecidaa; {numeros}')