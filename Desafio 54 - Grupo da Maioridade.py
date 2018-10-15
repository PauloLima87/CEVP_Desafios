from datetime import date

ma = 0
me = 0
for x in range(1, 8):
    ano = int(input(f'Ano de Nascimento {x}: '))
    if date.today().year - ano >= 18:
        ma+=1
    else:
        me+=1
print(f"""\n{ma} pessoas são maiores de idade 
{me} pessoas são menores de idade""")