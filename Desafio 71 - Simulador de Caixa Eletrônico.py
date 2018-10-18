print(f"""{'='*30}
{'BANCO CURSO EM VIDEO':^30}
{'='*30}""")
valor = int(input('Valor a ser sacado? '))
n50 = valor // 50
aux = valor % 50
n20 = aux // 20
aux = aux % 20
n10 = aux // 10
aux = aux % 10
n01 = aux
print(f"""\n\n{'-'*30}
{'SAQUE REALIZADO COM SUCESSO!':^30}
{'-'*30}
Notas de 50: {n50}
Notas de 20: {n20}
Notas de 10: {n10}
Notas de 01: {n01}
{'-'*30}
{'VOLTE SEMPRE!':^30}
{'-'*30}""")
