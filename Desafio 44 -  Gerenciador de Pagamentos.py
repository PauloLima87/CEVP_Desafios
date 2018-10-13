preco = float(input('Qual o valor final das compras?'))
print(f"""{'Formas de pagamento':=^60} 
        [ 1 ] A VISTA DINHEIRO
        [ 2 ] A VISTA CARTÃO
        [ 3 ] 2X NO CARTÃO
        [ 4 ] 3X OU MAIS NO CARTÃO""")
op = int(input( 'Qual a opção desejada?'))
if op == 1:
    print(f'Desconto de 10% R${preco*0.1}\nValor Final\nR${preco*0.9:.2f}')
elif op == 2:
    print(f'Desconto de 5% R${preco*0.05}\nValor Final\nR${preco*0.95:.2f}')
elif op == 3:
    print(f'Valor Final\nR${preco:.2f}\nEm duas parcelas de R${preco/2:.2f}')
elif op == 4:
    p = int(input('Em quantas parcelas gostaria de dividir (até 10x)'))
    if p > 10:
        print('Possivel parcelar em até 10x')
    else:
        print(f'Acrécimo de 20% R${preco*0.2}\nValor Final\nR${preco*1.2:.2f}')
        print(f'Em {p} prestações de R$ {(preco*1.2)/p:.2f}')
else:
    print('opção inválida!')