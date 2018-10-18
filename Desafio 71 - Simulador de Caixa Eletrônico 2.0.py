print(f"""{'='*30}
{'BANCO CURSO EM VIDEO':^30}
{'='*30}""")

valor = int(input('Valor a ser sacado'))
total = valor
ced = 50
qtdced = 0

while True:
    if total >= ced:
        total -= ced
        qtdced += 1
    else:
        if qtdced > 0:
            print(f'{qtdced} notas de {ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced ==10:
            ced =1
        qtdced = 0
        if total ==0:
            break