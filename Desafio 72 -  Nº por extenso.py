num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    op = int(input('Digite um numero de 0 a 20 [999 para finalizar]: '))
    if 0 <= op <= 20:
        print(f'Você digitou o numero {num[op]}')
    elif op == 999:
        break
    elif op > 20 or op < 0:
        print('Número inválido!')
