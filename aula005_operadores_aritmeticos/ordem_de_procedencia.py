# Arthur Braz Manai
# 16/04/2006

# Biblioteca 
import os

# horas
import datetime

# Terminal
os.system ('cls')

print ('=' * 70 )
print ('ENTRADAS DE DADOS')
print ('=' * 70 )

# Entrada
nota1 = float (input ('1ª nota :'))
nota2 = float (input ('2ª nota :'))
nota3 = float (input ('3ª nota :'))
nota4 = float (input ('4ª nota :'))

# Processamento

soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 /4
media_correta = (nota1 + nota2 + nota3 + nota4) /4

# Saida
print ('---NOTAS-----------')
print (F'Nota1: {nota1} / Nota2: {nota2} / Nota3: {nota3} / Nota4: {nota4} /')
print ('-' * 70 )
print (F'Media errada : {media}')
print (F'Media correta : {media_correta}')
print ('-' * 70 )