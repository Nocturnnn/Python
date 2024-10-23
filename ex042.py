reta1 = float(input('digite o comprimento da primeira reta: '))
reta2 = float(input('digite o comprimento da segunda reta: '))
reta3 = float(input('digite o comprimento da terceira reta: '))
verdade = True

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('essas retas podem sim formar um triângulo')
    verdade = True
else:
    print('essas retas não podem formar um triângulo')
    verdade = False

if verdade == True:
    if reta1 == reta2 == reta3:
        print('esse triângulo é equilátero')
    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('esse triângulo é isóceles')
    else:
        print('esse triângulo é escaleno')