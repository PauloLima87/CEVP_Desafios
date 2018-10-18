num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    op = int(input('Digite um numero de 0 a 20: '))
    if op <= 20:
        print(num[op])
    elif op >20:
        print('NUmero inválido!')
    elif op == 999:
        break