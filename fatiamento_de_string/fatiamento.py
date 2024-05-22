# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

# Biblioteca

import os

# Terminal

os.system('cls')

frase = 'String em Python!'

# Exibindo a string original =

print (f'String original.......: {frase}')

primeiros_cinco = frase[:5]
print (f'Primeiros 5 caracteres: {primeiros_cinco}')

ultimos_dez = frase[:-10]
print (f'Ultimos dez...........: {ultimos_dez}')

quarto_ao_decimo = frase[3:10]
print (f'Quarto ao decimo......: {quarto_ao_decimo}')

a_cada_dois = frase[::2]
print (f'A cada dois...........: {a_cada_dois }')

invertida = frase[::-1]
print (f'Invertida.............: {invertida}')
