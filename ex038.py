num = float(input('digite um valor: '))
num2 = float(input('digite outro valor: '))

if num > num2:
    print('o {} é maior que {}' .format(num, num2))
elif num == num2:
    print('o {} é igual há {}' .format(num, num2))
else:
    print('o {} é maior que {}' .format(num2, num))