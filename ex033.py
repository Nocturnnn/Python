num1 = float(input('digite o primeiro valor: '))
num2 = float(input('digite o segundo valor: '))
num3 = float(input('digite o terceiro valor: '))

if num1 > num2 and num1 > num3:
    print('o primeiro valor {} é o mais alto' .format(num1))

if num2 > num1 and num2 > num3:
    print('o segundo valor {} é o mais alto' .format(num2))

if num3 > num1 and num3 > num2:
    print('o terceiro valor {} é o mais alto' .format(num3))


if num1 < num2 and num1 < num3:
    print('o primeiro valor {} é o mais baixo' .format(num1))

if num2 < num1 and num2 < num3:
    print('o segundo valor {} é o mais baixo' .format(num2))

if num3 < num1 and num3 < num2:
    print('o terceiro valor {} é o mais baixo' .format(num3))