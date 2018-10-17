s = cont = 0
while True:
    n = int(input('nº: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f"""Soma: {s}
Foram digitados {cont} números""")
