# Curso de Desenvolvimento de Sistema
# Arthur Braz Monai
# 17/06/2024
# Atividade 007: Listas

import os

notas = []
nota_int = 0
num_ele = 0

while True:
    
    num_ele = num_ele + 1
    
    print ('digite s ou 0 para sair.....;')
    print ('digite r para resultado.....;')
    print ('digite m para media.........;')
    print ()
    print (notas)
    print ()
    nota = input('Insira a nota: ')
    os.system('cls')
   
    if nota.isdigit():
        nota_int = int(nota)
        notas.append(nota_int)

    if nota == 'r':
        os.system('cls')
        print(sum(notas))
        print(list(reversed(notas)))
        
    if nota == 'm':
        print(sum(notas) / num_ele)
        
    if nota == 's':
        os.system('cls')
        
        print('Programa finalizado!!!')
        break
    
  