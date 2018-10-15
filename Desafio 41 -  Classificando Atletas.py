import datetime
nascimento= 1
while True:
    nascimento = int(input('ano do Nascimento [0 para sair]: '))

    if datetime.date.today().year - nascimento <= 9:
        print(f'{datetime.date.today().year - nascimento} anos, categoria MIRIM')
    elif 9 < datetime.date.today().year - nascimento <= 14:
        print(f'{datetime.date.today().year - nascimento} anos, categoria INFANTIL')
    elif 14 < datetime.date.today().year - nascimento <= 19:
        print(f'{datetime.date.today().year - nascimento} anos, categoria JUNIOR')
    elif 19 < datetime.date.today().year - nascimento <= 25:
        print(f'{datetime.date.today().year - nascimento} anos, categoria SÊNIOR')
    elif nascimento == 0:
        break
    else:
        print(f'{datetime.date.today().year - nascimento} anos, categoria MASTER')
