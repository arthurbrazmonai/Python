# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 17/06/2024
# Atividade 007: Listas

import os
import random

os.system('cls')

num_es = []
num_so = []

for i in range(1,6):
    num_ess = int(input('Escolha 6 numeros: '))
    num_es.append(num_ess)
    
for c in range(1,6):
    num_sos = random.randint(1,1)
    num_so.append(num_sos)

print(f'numero sorteado {num_so}')
print(f'numero escolhido {num_es}')
print()

if num_so in num_es:
    print ('Voce ganhou!!!')
else:
    print ('Voce perdeu !!!')