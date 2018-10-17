cont = 0
soma = 0
num = int(input('Nº [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Nº [999 para parar]: '))

print(f"""Foram digitados {cont} numeros.
A soma dos numeros é {soma}""")
