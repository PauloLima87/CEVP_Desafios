prob = ' '
tota = totb = maiq = 0
print(f"""{'-'*35}
{'Massaria Store':^35}
{'-'*35}""")
while True:
    prod = str(input('Nome do produto: '))
    prec = float(input('Valor: R$ '))
    if totb == 0:
        totb = prec
        prob = prod
    #total da compra
    tota += prec
    #total de produtos com valor maior que R$1000,00
    if prec > 1000:
        maiq += 1
    #nome e valor do produto mais barato
    if prec < totb:
        totb = prec
        prob = prod
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if op =='N':
        break
print(f"""\n{'FIM DO PROGRAMA':-^35}
Total da compra: R${tota:.2f}
Existem {maiq} produtos de valor maior que R$1000,00
{prob} é o produto mais barato, e tem o valor de R$ {totb:.2f}""")