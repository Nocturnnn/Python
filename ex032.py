ano = int(input('digite um ano: '))
ano4 = ano % 4
ano100 = ano % 100
ano400 = ano % 400

if ano4 == 0 and ano100 == 0 and ano400 != 0:
    print('esse ano não bissexto')
elif ano4 == 0:
    print('esse ano é bissexto')
else:
    print('esse ano não é bissexto')