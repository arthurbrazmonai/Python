# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

# Biblioteca

import os

# Terminal

os.system ('cls')

print ('='* 70)
print ('ESTUDO DE CONDICIONAL: PARTE 1')
print ('='* 70)

# Entrada 

salario1 = int (input ('insira o salario1 atual: '))
salario1r = 0

salario2 = int (input ('insira o salario2 atual: '))
salario2r = 0

# Condicional

if salario1 > 1500 and salario1 > 0:
    salario1r = (salario1 // 5) + salario1
    print (f'Salario com o aumento sera de: {salario1r}')
else:  
    print ('Erro!!!')
    

if salario1 < 1000 and salario1 > 0:
    salario2r = (salario2 // 10) + salario2
    print (f'Salario com o aumento sera de: {salario2r}')
else:  
    print ('Erro!!!')
    