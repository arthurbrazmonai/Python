# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 18/04/2024
# Calculo de Perimeto

# Biblioteca

import os
import math

# Terminal

os.system('cls') 

# Declaraçoes 

base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5
ca  = 10

# Processamento
potencia = math.pow(base, expoente)
raizQuadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseso = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

# Saida
print (f'{base} elevado a {expoente} e igual a: {potencia}')
print (f'A raiz quadrada de {radicando} e: {raizQuadrada}')
print (f'O seno de {angulo} e: {seno:.2f}')
print (f'O cosseno de {angulo} e: {cosseso:.2f}')
print (f'A tagente de {angulo} e: {tangente:.2f} ')
print (f'O valor de hipotenusa e: {hipotenusa:.2f}')