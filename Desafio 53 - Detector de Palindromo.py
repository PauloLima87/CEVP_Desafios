txt = str(input('Frase: ')).strip().upper() #joga a entrada para maiusculas e elimina espaços no inicio e fim da sentença
print(f'Frase digitada:\n{txt}')
palavras = txt.split() #separa as palavras pelos espaços dentro de uma lista
junta = ''.join(palavras) #junta a lista em uma variavel utilizando o caractere entre parenteses como separador (neste caso vazio)
print(junta)
inver = ''
for x in range(len(junta) - 1, -1, -1):#leitura do tamanho -1 (index começa em 0), ate antes da primeira(-1), voltando(-1)
    inver += junta[x]
print(inver)
if inver == junta:
    print('\n\033[33mé Palindromo')
else:
    print('\n\033[32mNão é Palindromo')