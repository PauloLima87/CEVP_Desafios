from time import sleep

op = 0
n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

while op!= 5:
    op = int(input(""""O Que deseja fazer?
    [1] Somar
    [2] Multipicar
    [3] Maior
    [4] Novos Numeros
    [5] sair
    QUAL SUA OPÇÃO: """))
    if op == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif op == 2:
        print(f'{n1} X {n2} = {n1*n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif op == 4:
        n1 = int(input('Novo Valor 1: '))
        n2 = int(input('Novo valor 2: '))
    elif op == 5: #apenas para correção de Bug
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção Inválida! Tente novamente.')
    print('='*15)
    sleep(2)

print('='*15)
print('FIM DO PROGRAMA')