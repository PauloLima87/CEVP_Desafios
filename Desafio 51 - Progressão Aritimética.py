
print(f'{"10 Termos da PA":=^30}')

print(f'{"Primeira maneira":=^20}')
t1 = int(input('1º Termo: '))
t = t1
r = int(input('Razão: '))
for x in range (1, 11):
    print(f'{x}º: {t1}', end="  |  ")
    t1+= r

print(f'\n\n{"Segunda maneira":=^20}')
t10 = t+(10-1)*r #calculando o termo 1q0 da PA
for c in range (t, t10 + r, r): #paramentros saem de t inicial até o valor de t10 + r com passos de valor R (razão)
    print(f'{c}', end="  |  ")
