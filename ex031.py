km = float(input('quantos KM foi sua viagem? '))

if km <= 200:
    preco = km * 0.5
    print('sua viagem custa {:.2f}R$' .format(preco))
elif km > 200:
    preco = km * 0.45
    print('sua viagem custa {:.2f}R$' .format(preco))