num = int(input('Numero: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[32m', end=" ")
        cont += 1
    else:
        print('\033[34m', end=" ")
    print(f'{c}', end=" ")
if cont > 2:
    print(f'\n\033[mO numero {num} é divisível por {cont} valores.\nLogo, \033[31mNÃO É PRIMO')
else:
    print(f'\n\033[mO número {num} é divisível por 1 é por ele mesmo.\nLogo, \033[34mÉ PRIMO')
