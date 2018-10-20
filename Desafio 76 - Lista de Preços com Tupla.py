lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(f"""{'='*35}
{'LISTA DE PREÇOS':^35}
{'='*35}""")
for x in range (0, len(lista)):
    if x % 2 == 0:
        #print(f'{lista[x]:.<30}', end="."') maneira 1
        print(f'{lista[x]:.<24}', end=".")
    else:
        #print(f'{"R$":.>15}{lista[x]:>7}') maneira 1
        print(f'R$ {lista[x]:>7.2f}') #Maneira dois
print(f"""{'='*35}
{'='*35}""")
