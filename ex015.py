import emoji
km = float(input('informe os km rodados do carro: '))
dias = int(input('informe por quantos dias o carro foi alugado: '))
dias = dias * 60
km = km * 0.15
total = km + dias
print('o total a ser pago é {}R$ 😎' .format(total))