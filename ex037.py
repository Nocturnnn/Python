num = float(input('digite um valor: '))
print('digite 1 para conversão em binario')
print('digite 2 para conversão em octal')
print('digite 3 para conversão em hexadecimal')

valor = float(input('digite o número de coneversão: '))

if valor == 1:
    while num != 0 and num > 0:
        print(num)
        num = num % 2