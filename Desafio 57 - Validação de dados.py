sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
print(sexo)
while sexo not in 'FM':
    sexo = str(input("""Dados Inválidos!
    Digite novamente
    Sexo [F/M]: """)).strip().upper()[0]
print(f'Registrado com Sucesso!\nSexo: {sexo}')