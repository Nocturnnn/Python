soma = 0
for i in range(0, 6):
    num = int(input('digite um número: '))
    if num % 2 != 0:
        soma = soma + num
print('o números impares digitados possuem em soma total o valor {}' .format(soma))