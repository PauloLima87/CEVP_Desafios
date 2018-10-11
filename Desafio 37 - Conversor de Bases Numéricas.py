op = 4
while True:

    if op == 1:
        print(f'Binário: {bin(numero)}')
    elif op == 2:
        print(f'Octal: {oct(numero)}')
    elif op == 3:
        print(f'Hexadecimal: {hex(numero)}')
    elif op ==4:
        numero = int(input('Qual numero será convertido? '))
    elif op == 0:
        aux = str(input('Deseja parar as conversões [S/N] ?')).strip()
        if aux in 's S sim SIM Sim':
            break
    else:
        print('\n======Opção inválida!======\n')
    op = int(input(f"""PARA QUE BASE DESEJA CONVERTER O NUMERO {numero}?
       [1] Binário
       [2] Octal
       [3] Hexadecimal
       [4] NOVO NUMERO
       [0] SAIR\nR = """))
