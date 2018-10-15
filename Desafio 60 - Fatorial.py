print(f'{"Primeira Resolução":=^20}\n')
from math import factorial
f = int(input('Deseja calcular o fatorial de qual numero? '))
fat = 0
for x in range(f,0,-1):
    print(f'{x}', end=' ')
    fat = factorial(f)
print('= ', fat)

print(f'\n\n{"Segunda resolução":=^20}')
f = int(input('Deseja calcular o fatorial de qual numero? '))
c = f
n = 1
while c > 0:
    print(f'{c}', end=" ")
    print(' X ' if c > 1 else '=', end= " ")
    n *= c # equivale a n = n * c onde c é o numeroi desejado e n inicia em 1
    c-= 1
print(n)
