tabela = ('Palmeiras', 'Internacional', 'Flamengo', 'São Paulo', 'Grêmio', 'Atlético-MG',
          'Santos', 'Atlético-PR', 'Fluminense', 'Cruzeiro', 'Corinthians', 'Botafogo',
          'Bahia', 'Vasco', 'América-MG', 'Vitória', 'Ceará', 'Chapecoense',
          'Sport', 'Paraná')

print(f"""{'='*30}
{'TABELA DO BRASILEIRÃO':^30}
{'='*30}""")
print(tabela)
print(f"""{'='*30}
{'5 PRIMEIROS':^30}
{'='*30}""")
print(tabela[:5])
print(f"""{'='*30}
{'4 ULTIMOS':^30}
{'='*30}""")
print(tabela[-4:])
print(f"""{'='*30}
{'TABELA EM ORDEM ALFABÉTICA':^30}
{'='*30}""")
print(sorted(tabela))
print(f"""{'='*30}
{'ONDE ESTÁ A CHAPECOENSE?':^30}
{'='*30}""")
print(f'A Chapecoense está em {tabela.index("Chapecoense")+1}º lugar')