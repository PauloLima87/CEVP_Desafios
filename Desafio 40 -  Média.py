n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))

if (n1+n2)/2 >= 7:
    print(f'\n{"PARABÈNS! VOCÊ FOI APROVADO":=^80}\n\nSua Média final foi: {(n1+n2)/2}')
elif (n1+n2)/2 >= 5 and (n1+n2)/2 <= 6.9:
    print(f'\n{"VOCÊ ESTA DE RECUPERAÇÃO":=^80}\n\nSua Média final foi: {(n1+n2)/2}')
else:
    print(f'\n{"VOCÊ ESTA REPROVADO":=^80}\n\nSua Média final foi: {(n1+n2)/2}')
