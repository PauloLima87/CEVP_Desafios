from datetime import date


ano = int(input('Em qu ano você nasceu?'))

if date.today().year - ano < 18:
    if abs(18-(date.today().year - ano)) > 1:
        print(f'Ainda não é hora de se alistar? faltam {abs(18-(date.today().year - ano))} anos')
    else:
        print(f'Ainda não é hora de se alistar? falta {abs(18-(date.today().year - ano))} ano')
elif date.today().year - ano > 18:
    if abs(18-(date.today().year - ano)) > 1:
        print(f'Já passou seu período de aistamento? Atraso de  {abs(18-(date.today().year - ano))} anos')
    else:
        print(f'Já passou seu período de aistamento? Atraso de {abs(18-(date.today().year - ano))} ano')
else:
    print('Hora de se alistar! procure uma junta de serviço militar')