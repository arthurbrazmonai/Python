# Arthur Braz Monai
# 18/04/2024

# Biblioteca 

import os

# Terminal

os.system ('cls')

# Variaveis/Entrada

nota1 = float (input ('Insira a nota1:'))
nota2 = float (input ('Insira a nota2:'))
nota3 = float (input ('Insira a nota3:'))
nota4 = float (input ('Insira a nota4:'))

# Processamento

soma = nota1 + nota2 + nota3 + nota4
media = soma/4

# Saida

print (F'A soma das notas = {soma}, A media = {media}')