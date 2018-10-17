op = 'S'
soma = cont = 0
while op in 'S':
    num = int(input('nº: '))
    soma += num
    cont += 1
    op = str(input('Deseja continuar? [S/N] ')).upper()[0]
print(f"""Voce digitou {cont} nºs.
A soma dos valores é {soma}
a media dos valores digitados é {soma/cont}""")