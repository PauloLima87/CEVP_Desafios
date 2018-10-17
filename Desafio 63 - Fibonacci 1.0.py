print(f'{"-"*30}\n{"Sequencia de Fibonacci":^30}\n{"-"*30}')
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
cont = 2
print(f'{0} - {1}', end='')
while cont < n:
    aux = t1 + t2
    print(f"\033[m - {aux}", end="")
    t1 = t2
    t2 = aux
    cont += 1
print('- FIM')