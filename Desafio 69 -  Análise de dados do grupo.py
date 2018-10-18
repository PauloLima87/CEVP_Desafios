mid = hom = m20 = 0
while True:
    idade = int(input('Idade: '))
    # pessoas com mais de 18
    if idade >= 18:
        mid += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('OPÇÂO INVÀLIDA')
    #homens
    if sexo == 'M':
        hom += 1
    #mulheres com menos de 20
    if sexo == 'F' and idade < 20:
        m20 += 1
    op = str(input('Deseja Cadastrar uma nova pessoa?[S/N]')).strip().upper()[0]
    if op == 'N':
        break
print(f"""Existem {mid} pessoas maiores de idade.
{hom} dos cadastrados são homens.
{m20} mulheres cadastradas possuem menos de 20 anos""")