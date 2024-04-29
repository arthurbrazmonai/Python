# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 26/04/2024

# Biblioteca

import os

# Terminal

os.system ('cls')

print ('='* 70)
print ('EXERCICIO DE CONDICIONAL: F')
print ('='* 70)

# Entrada

ano = int (input ('Insira o ano: '))

# Condicional 

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print (f'O ano {ano} e bissexto')
else:
    print (f'O ano {ano} nao e bissexto')