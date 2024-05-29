import os 

os.system('cls')

for c in range(1, 11):
    if c == 5:
        print(f'O numero {c} esta fora do loop')
        continue
    
    print(f'o numero e {c}')