from random import randint

num1 = randint(0,10)
num2 = randint(0,10)
num3 = randint(0,10)
num4 = randint(0,10)
num5 = randint(0,10)

sorteio = (num1, num2, num3, num4, num5)

print(sorteio)

cont = maior = menor = 0

for cont in range(0, len(sorteio)):
    if cont == 0:
        maior = sorteio[cont]
        menor = sorteio[cont]
    else:
        if menor > sorteio[cont]:
            menor = sorteio[cont]
        if maior < sorteio[cont]:
            maior = sorteio[cont]

print(f'o maior número sorteado é {maior}')
print(f'o menor número sorteado é {menor}')