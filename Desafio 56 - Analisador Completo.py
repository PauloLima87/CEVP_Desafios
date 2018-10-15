medIdade = 0
hMv = 0
m20 = 0
for pessoa in range(1, 5):
    print(f'===== Pessoa {pessoa} =====')
    nome = str(input(f'Nome {pessoa}: ')).strip()
    idade = float(input(f'Idade {pessoa}: '))
    sexo = str(input(f'Sexo [F\M]: ')).strip().capitalize()
    medIdade += idade
    if sexo[0] == 'M' and idade > hMv:
        nomeMv = nome
        hMv = idade
    if sexo[0] == 'F' and idade < 20:
        m20 += 1
print(f"""A média de idade do grupo é {medIdade/4} anos
O homem mais velho é {nomeMv} e tem {hMv:.0f} anos
Por fim , existem {m20} mulheres menores de 20 anos""")