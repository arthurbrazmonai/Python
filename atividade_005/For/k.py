import os 

os.system('cls') 

palavra = input ('Digite uma palavra: ')
palavrai = palavra [::-1]
print (palavrai)

if palavrai == palavra:
    print(f'A palavra {palavra} e um palindromo !!!')
else:
    print (f'A palavra {palavra} nao e um palindromo !!!')