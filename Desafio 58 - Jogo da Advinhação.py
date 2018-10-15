from random import randint
tent = 1
print(f"""{"Jogo da Advinhação":=^30}
Olá! Acabei de pensar em um numero,
de 0 a 10, consegue adivinhar qual é?""")
com = randint(1, 10)
print(com)
palpite = int(input('Palpite:'))
while com != palpite:
    if palpite > com:
        palpite = int(input(f'Menos...\nTente novamente: '))
        tent+=1
    elif palpite < com:
        palpite = int(input(f'Mais...\nTente novamente: '))
        tent+=1
if tent == 1:
    print('Parabṕens! Você acertou de Primeira')
else:
    print(f'Parabéns!! Você acertou em {tent} tentativas')