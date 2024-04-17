# Arthur Braz Manai
# 16/04/2006

# Biblioteca 
import os

# horas
import datetime

# Terminal
os.system ('cls')

# Imput
nome = input('insira o nome: ')
peso = input ('peso:')
altura = input('altura:')

# Casting
nascimento = int (input('Ano de Nascimento: '))
cep = int (input ('CEP:'))
bairro = str (input('Bairro:'))
rua = str (input ('Rua:'))
numero = int (input('Numero:'))

# Processamente de dados
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# Saida
print ('=' * 70 )
print ('ENTRADAS DE DADOS')
print ('=' * 70 )

print ('nome............;' , nome)
print ('nascimento......;' , idade)
print ('peso............;' , peso, 'kg')
print ('altura..........;', altura, 'M')

# Saida Interpolada
print (F'seu nome e {nome}, voce tem {idade} anos!')
print (F'CEP..............: {cep}')
print (F'Bairro..............: {bairro}')
print (F'Rua..............: {rua}')
print (F'Numero..............: {numero}')
print ('_' * 70 )




