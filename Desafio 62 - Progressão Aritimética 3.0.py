print(f'\n\n{"Gerador de PA 2":=^20}')
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
aux = 1
total = 0
mais = 10
cont = 0
t1 = t #guardar o valor de t1 para obter a soma da PA
while mais != 0:
    total += mais
    while aux <= total:
        print(f'\033[32mT{aux}: \033[m{t}', end=" ")
        t += r #t deixa de ser o T1 e passa a ser o parametro utilizado para formar todos os termos da PA
        aux += 1
    print('\033[31mPAUSA')
    mais = int(input('\033[mQuantos termos deseja adicionar? '))
    cont += mais

a = t1 + (t1 + ((total - 1) * r))
b = a * total
c = b / 2
print(f"""Voce adicionou mais \033[32m{cont} \033[mtermos,
de um total de \033[32m{total}\033[m termos,\nSoma dos termos da PA\nS{total} = {c}
\n\033[31mFIM DO PROGRAMA""")
