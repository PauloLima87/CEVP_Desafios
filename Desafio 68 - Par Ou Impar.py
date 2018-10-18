from random import randint
cont = 0
while True:
    nm = int(input('Qual o Número?'))
    op = str(input('Par ou Impar? [P/I]')).upper()[0].strip()
    cm = randint(0, 11)
    print('\nDEU PAR\n' if (nm + cm)% 2 == 0 else '\nDEU IMPAR\n')
    if op == 'P':
        if (nm + cm) % 2 == 0:
            print(f"""VOCÊ: {nm} X {cm} COM
            Voce ganhou!!""")
        else:
            print(f"""VOCÊ: {nm} X {cm} COM
            Voce Perdeu!!""")
            break
    elif op == 'I':
        if (nm + cm) % 2 !=0:
            print(f"""VOCÊ: {nm} X {cm} COM
            Voce ganhou!!""")
        else:
            print(f"""VOCÊ: {nm} X {cm} COM
            Voce Perdeu!!""")
            break
    else:
        print('Opção Inválida!')
    cont += 1
print(F"""\n{'PLACAR FINAL':=^35}
VOCÊ VENCEU {cont}\n{'='*35}""")
