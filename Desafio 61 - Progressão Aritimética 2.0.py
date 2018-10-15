print(f'{"Gerador de PA 1":=^20}')
t1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
t10 = t1 + (10 - 1) * r
aux = 1
while t1 != t10 + r:
    print(f'\033[32mT{aux}: \033[m{t1}', end=" ")
    t1 += r
    aux += 1

print(f'\n\n{"Gerador de PA 2":=^20}')
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
aux = 1
while aux <= 10:
    print(f'\033[32mT{aux}: \033[m{t}', end=" ")
    t += r
    aux += 1
