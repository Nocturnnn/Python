maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('digite o peso da {}° pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('o maior peso lido foi de {}(kg)' .format(maior))
print('o menor peso lido foi de {}(kg)' .format(menor))