palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for x in palavras:
    print(f'\nNa palavra {x.upper()} temos...', end=' ')
    for letra in x:  # Python identifica cada sequencia de caracteres como uma lista, logo é possivel percorrer cada
        # termo da tupla por letras individuais
        if letra.lower() in 'a e i o u': #Percorrendo o termo da tupla buscando as vogais
            print(letra, end=" ")
