resp = 5
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('digite um número: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('você digitou {} números e a média foi {}.' .format(quant, media))
print('o maior valor foi {} e o menor foi {}.' .format(maior, menor))