casa = float(input('Qual o valor do imóvel desejado? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos deseja quitar seu imóvel? '))
print(f"""Valor financiado: {casa}
Prazo = {anos} anos
N° de parcelas: {anos*12}
Valor Maximo permitido: {salario*0.3}
VALOR PARCELA: {(casa/(anos*12)):.2f}""")

if (casa / (anos * 12)) > (salario * 0.3):
    print('\n\n{:=^60}\n\n'.format('FINANCIAMENTO NEGADO'))
    print('VALOR DA PARCELA: {:.2f}\nSua parcela não pode exeder o valor de R${:.2f}'.format(casa / (anos * 12),
                                                                                             salario * 0.3))
else:
    print(f'\n\n{"FINANCIAMENTO APROVADO":=^60}\n\n')
    print('PARABÈNS! Sua parcela é de R${:.2f}'.format((casa / (anos * 12))))
