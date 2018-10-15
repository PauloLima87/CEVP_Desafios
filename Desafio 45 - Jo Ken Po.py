import random
from time import sleep

op = ''
j1 = 0
j2 = 0
while True:
    print(f'\n{"PLACARA DA RODADA":=^60}\nJogador: {j1} X Computador {j2}\n{"="*60}\n\n')
    print("""    [ 1 ] Pedra
    [ 2 ] Papel
    [ 3 ] Tesoura
    [ 0 ] PARAR DE JOGAR\n""")
    palpite = int(input('Pedra, papel ou tesoura? \n\n'))
    com = random.randint(1, 3)
    if palpite != 0:
        print('Jo')
        sleep(1)
        print('Ken')
        sleep(1)
        print('Po')
    if palpite == com:
        if palpite == 1:
            print('Ambos escolehram Pedra')
        elif palpite == 2:
            print('Ambos escolheram Papel')
        elif palpite == 3:
            print('Ambos escolheram Tesoura')
        print('Vocês Empataram')
    elif palpite == 1 and com == 2:
        print('Jogador: PEDRA\nComputador: PAPEL')
        print('Você perdeu! Papel vence Pedra')
        j2 += 1
    elif palpite == 1 and com == 3:
        print('Jogador: PEDRA\nComputador: TESOURA')
        print('Você Venceu! Pedra quebra Tesoura')
        j1 += 1
    elif palpite == 2 and com == 1:
        print('Jogador: PAPEL\nComputador: PEDRA')
        print('Você Venceu! Papel embrulha Pedra')
        j1 += 1
    elif palpite == 2 and com == 3:
        print('Jogador: PAPEL\nComputador: TESOURA')
        print('Você perdeu! Tesoura corta papel')
        j2 += 1
    elif palpite == 3 and com == 1:
        print('Jogador: TESOURA\nComputador: PEDRA')
        print('Você Perdeu! Pedra quebra Tesoura')
        j2 += 1
    elif palpite == 3 and com == 2:
        print('Jogador: TESOURA\nComputador: PAPEL')
        print('Você Venceu! Tesoura corta Papel')
        j1 += 1
    elif palpite == 0:
        op = str(input('Deseja mesmo sair [s/n]? '))
        if op in 'S s sim SIM SIm SiM Sim sIM sIm siM':
            print('FIM DO JOGO')
            break
    else:
        print('Opção Inválida!')
if j1 > j2:
    print('Parabéns Jogador, você venceu!')
else:
    print('Tente novamente, Computador foi o vencedor')
