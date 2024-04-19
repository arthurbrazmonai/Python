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

# Entrada de dados

print ('--- SOMA ')
print ('-' * 70)

parcela_1 = float (input ('entre com a parcela 1 ...'))
parcela_2 = float (input ('entre com o parcela 2...'))

print ('--- SUBTRAÇAO ')
print ('-' * 70)

minuendo = float (input ('entre com o diminuendo...'))
subtraendo = float (input ('entre com o subtraendo...'))

print ('--- PRODUTO ')
print ('-' * 70)

multiplicando = float (input ('entre com o multiplicador...'))
multiplicador = float (input ('entre com o multipicador...'))

print ('--- DIVISAO ')
print ('-' * 70)

dividendo = float (input ('entre com o dividendo...'))
divisor = float (input ('entre com o divisor...'))

# Processamento

soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
conciente = dividendo / divisor

# Saida Interpolada
print (F'A soma de {parcela_1} + {parcela_2} e = {soma}')
print (F'A subtraçao de {minuendo} - {subtraendo} e = {diferenca}')
print (F'A multiplicaçao de {multiplicando} x {multiplicador} e = {produto}')
print (F'A divisao de {dividendo}  ÷ {divisor} e = {conciente}')