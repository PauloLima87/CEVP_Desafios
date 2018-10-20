tupla = (int(input('1º Numero: ')), int(input('2º Numero: ')), int(input('3º Numero: ')), int(input('4º Numero: ')))
par = 0
print(f'Tupla digitada: {tupla}')
if tupla.count(9)!=0:
    print(f'O número 9 é encontrado {tupla.count(9)}x na tupla')
else:
    print('Numero 9 não encontrado')
if 3 in tupla:
    print(f'O numero 3 aparece na posição {tupla.index(3)}')
else:
    print('O numero 3 não foi digitado')
print('Os Números pares digitados são: ', end=" ")
for x in tupla: #analisa com X o valor e não o indice
    if x % 2 ==0:
        par += 1
        print(f'{x}', end=" ")
if par > 1:
    print(f'\n{par} numeros são pares')
elif par == 1:
    print(f'\n{par} numero é par')
else:
    print('(Não existem números pares)')
