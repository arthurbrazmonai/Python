import os 

os.system('cls')

contador = 1

while contador < 7:
    print(f'Contador e:', contador)
    contador += 1
    
    if contador == 4:
        print(f'Contador chegou em {contador};tBreak no while!')
        break
else:
    print('while finalizado!')