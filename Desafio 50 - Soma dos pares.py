soma = 0
for c in range(1, 7):
    num = int(input('Valor: '))
    if num % 2 == 0:
        soma += num
print(f'Soma dos numeros pares é {soma}')