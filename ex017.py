import math
catetoOposto = float(input('informe o cateto oposto: '))
catetoAdjasente = float(input('informe o cateto adjasente: '))
hipotenusa = (catetoOposto ** 2) + (catetoAdjasente ** 2)
print('sua hipotenusa é: {}' .format(math.sqrt(hipotenusa)))