import os


os.system('cls')

lista_aluno = []

for c in range (0,5):
    nome = str(input('Entre com o nome do aluno: '))
    
    lista_aluno.append(nome)
    
for aluno in range(len(lista_aluno)):
    print(lista_aluno[aluno], end='')
    if c ==3:
        print()