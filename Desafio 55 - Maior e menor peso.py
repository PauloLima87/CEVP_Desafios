maP = 0
meP = 0
aux = 1
op =''
while op in 'sim sIm sIM siM SIM Sim SiM SIm s S':
    peso =float(input(f'Peso da pessoa {aux}: '))
    if aux == 1:
        maP = peso
        meP = peso
    else:
        if peso > maP:
            maP = peso
        if peso< meP:
            meP = peso
    op = str(input('Deseja Digitar outro peso? [S/N]'))
    aux+=1
print(f"""O maior peso é {maP}
O menor peso é {meP}""")