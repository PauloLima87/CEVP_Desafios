print(f'{"Indice de Massa Corporal":=^60}')
peso = float(input('Peso (Kg): '))
altura = float(input('ALtura (m): '))
print(f"""\n{'Dados pessoais':*^60}\nPeso: {peso} kg
Altura: {altura} m
IMC: {(peso/(altura**2)):.2f}\n{'*'*60}\n""")
if (peso / (altura ** 2)) <= 18.5:
    print('Você se encontra ABAIXO DO PESO IDEAL')
elif 18.5 < (peso / (altura ** 2)) <= 25:
    print('Você se encontra NO PESO IDEAL')
elif 25 < (peso / (altura ** 2)) <= 30:
    print('Você se encontra NA FAIXA DE SOBREPESO')
elif 30 < (peso / (altura ** 2)) <= 40:
    print('Você se encontra NA FAIXA DE OBESIDADE')
else:
    print('Você se encontra NA FAIXA DE OBESIDADE MÓRBIDA')
print(f'Seu peso ideal é no máximo {25*(altura**2):.2f} Kg\nVocê precisa perder {peso-(25*(altura**2)):.2f} Kg')