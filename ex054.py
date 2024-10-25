import datetime
data = datetime.datetime.now().year
quantidadeMaior = 0
quantidadeMenor = 0
for i in range(1, 8):
    ano = int(input('em qual ano a {}° pessoa nasceu? ' .format(i)))

    if data - ano >= 18:
        print('a {}° pessoa é maior de idade tendo {} anos' .format(i, data - ano))
        quantidadeMaior += 1
    else:
        print('a {}° pessoa não é maior de idade tendo {} anos' .format(i, data - ano))
        quantidadeMenor += 1
print('há {} pessoas maiores de idade' .format(quantidadeMaior))
print('há {} pessoas menores de idade' .format(quantidadeMenor))