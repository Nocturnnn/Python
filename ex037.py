num = int(input('digite um valor: '))

print('digite 1 para conversão em binario')
print('digite 2 para conversão em octal')
print('digite 3 para conversão em hexadecimal')

valor = float(input('digite o número de coneversão: '))

if valor == 1:
    print('seu número em binário é {}' .format(bin(num)))
elif valor == 2:
    print('seu número em octal é {}' .format(oct(num)))
elif valor == 3:
    print('seu número em hexadecimal é {}' .format(hex(num)))
else:
    print('digite 1,2 ou 3 seu verme')