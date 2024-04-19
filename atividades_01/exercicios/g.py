# Arthur Braz Monai
# 18/04/2024

# Biblioteca 

import os

# Terminal

os.system ('cls')

# Variaveis/Entrada
valorm = float (input ('Inserir o valor em M: '))

# Pocessamento

resultadocm = valorm/100
resultadomm = valorm/1000

# Saida 

mensagem = print (F'Resultado : {resultadocm} CM')
mensagem = print (F'Resultado : {resultadomm} MM')
