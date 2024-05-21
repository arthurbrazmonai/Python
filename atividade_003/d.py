# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Atividade D

# Biblioteca

import os
import math

# Terminal

os.system('cls')

# Receber 

angulo = float (input('Informe o angulo: '))

# Processamento

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Saida 

print (f'O seno do angulo {angulo} e ......; {seno:.2f}')
print (f'O cosseno do angulo {angulo} e ......; {cosseno:.2f}')
print (f'O tagente do angulo {angulo} e ......; {tangente:.2f}')

