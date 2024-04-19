# Arthur Braz Monai
# 18/04/2024

# Biblioteca

import os
import datetime

# Terminal 

os.system ('cls')

# Variaveis/Entrada

ano_nas = int (input ('Ano de nascimento: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nas 

# Saida

print ('=' * 70 )
print ('Idade de usuario: ')
print ('-' * 70 )

mensagem = print (F'Sua idade e: {idade}')
print ('-' * 70 )