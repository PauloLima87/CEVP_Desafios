print(f'{"Tabudada 3.0":=^35}')
while True:
    num = int(input('Quer ver a tabuada de qual Numero? '))
    if num < 0:
        break
    for x in range(0, 11):
        print(f'{num} X {x:2} = {num*x}')
    print('='*35)
print(f'{"Tabudada 3.0 Encerrado":=^35}')
