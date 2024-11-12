total = totmil = menor = cont = 0
while True:
    produto = str(input('nome do produto: '))
    preco = float(input('preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('{:-^40}' .format('Fim do Programa'))
print(f'o total foi de R${total:.2f}')
print(f'temos {totmil} produtos custando mais de R$1000.00')
print(f'o produto mais barato custa R${menor:.2f}')