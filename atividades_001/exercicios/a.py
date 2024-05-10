# Arthur Braz Monai
# 18/04/2024

# Biblioteca 

import os

# Terminal

os.system ('cls')

# Variaveis/Entrada
valor1 = float (input ('inserir o primeiro valor: '))
valor2 = float (input ('iserir o segundo valor: '))
valor3 = float (input ('inserir o terceiro valor: '))

# Processamento
resultado_soma = valor1 + valor2 + valor3
resultado_multipli = valor1 * valor2 * valor3

# Saida
print ('=' * 70 )
print ('Calculos soma/multi')
print ('-' * 70 )
print ()

mensagem = print (F'Resultado : {resultado_soma}')
mensagem = print (F'Resultado : {resultado_multipli}')
print ('-' * 70 )