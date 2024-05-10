# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

# Biblioteca

import os
from datetime import datetime
from datetime import date

# Terminal

os.system('cls') 

# Declarando variavel para data
data = datetime.now()

# Declarando uma variavel data formatada 
data_formatada = data.strftime('%d/%m/%Y')

# Declarando uma variavel data formatada 
data_hora_formatada = data.strftime('%d/%m/%Y %H:%M')

print(f'Data formatada: {data_formatada}')
print(f'Data e hora  formatadas: {data_hora_formatada}')

# Recebendo o ano

data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

# Imprimindo a data atual eo nascimento

print(f'Data atual no sistema: {data_atual}')
print(f'Nascimento...........: {nascimento}')
# Imptimindo so o ano
print(f'Ano atual............: {data_atual.year}')
# Imprimindo so a idade
print(f'Sua idade e..........: {idade} anos')

