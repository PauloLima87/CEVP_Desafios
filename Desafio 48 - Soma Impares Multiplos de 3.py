soma = 0
cont = 0
for c in range(1, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            cont += 1
            soma += c
print(f'1ª Resposta: A soma de todos os {cont} Numeros impares e multiplos de 3 é {soma}')

soma2 = 0
cont2 = 0
for c in range(1, 500, 2):  # andando de 2 em 2 já será análisado apenas os ímpares
    if c % 3 == 0:
        cont2 += 1
        soma2 += c
print(f'2ª Resposta: A soma de todos os {cont} Numeros impares e multiplos de 3 é {soma}')
