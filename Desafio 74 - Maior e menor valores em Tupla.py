import random

num = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
ma = me = 0

for x in range(0, len(num)):
    if num[x] > ma:
        ma = num[x]
    if num[x] < me:
        me = num[x]
    if x == 1:
        me = ma

print(f"""\n{'UTILIZANDO FOR':-^35}
Tupla sorteada: {num}
O maior número é {ma}
o menor número é {me}""")

print(f"""\n{'UTILIZANDO METODOS MIN E MAX':-^35}
Tupla sorteada: {num}
O maior número é {max(num)}
o menor número é {min(num)}""")

