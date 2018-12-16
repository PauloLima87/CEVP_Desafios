valor = list()
menor = maior = 0
for i in range(0, 5):
    valor.append(int(input(f'Valor {i + 1}: ')))
    if i == 1:
        maior = menor = valor[i]
    else:
        if valor[i] > maior:
            maior = valor[i]
        if valor[i] < menor:
            menor = valor[i]

print(f'\nf = {valor}\n')
print(f"O Menor valor é {menor} nas posições ", end='')
for a, b in enumerate(valor):
    if b == menor:
        print(f'{a}.. ', end='')
print()
print(f"O Maior valor é {maior} nas posições ", end='')
for a,b in enumerate(valor):
    if b == maior:
        print(f'{a}.. ', end='')
