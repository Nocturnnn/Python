nascimento = int(input('digite o ANO de nascimento do atleta: '))

from datetime import date

atual = date.today().year

idade = atual - nascimento
if idade <= 9:
    print('MIRIM')
elif idade < 14 and idade >= 9:
    print('INFANTIL')
elif idade >= 14 and idade < 19:
    print('JUNIOR')
elif idade >= 19 and idade < 25:
    print('SÊNIOR')
else:
    print('MESTRE')