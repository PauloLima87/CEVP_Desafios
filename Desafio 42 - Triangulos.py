l1 = int(input('Lado 1: '))
l2 = int(input('lado 2: '))
l3 = int(input('lado 3: '))

if l1 + l2 > l3 and l1 + l3 >l2 and l2 + l3 > l1:
    print(f'os valores {l1},{l2} e {l3} formam triângulo')
    if l1 == l2 == l3 == l1:
        print('Triângulo EQUILATERO')
    elif l2 != l1 != l3 != l2:
        print('Triângulo ESCALENO')
    else:
        print('Triangulo ISÒCELES')
else:
    print(f'os valores {l1},{l2} e {l3} não formam triangulo')