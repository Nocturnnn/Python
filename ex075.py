num1 = int(input('valores: '))
num2 = int(input('valores: '))
num3 = int(input('valores: '))
num4 = int(input('valores: '))

tupla = (num1, num2, num3, num4)

valor9 = posicao = 0

for i in range(0, len(tupla)):
    if tupla[i] == 9:
        valor9 += 1

    if tupla[i] == 3:
        posicao = i

    if tupla[i] % 2 == 0:
        print(f'o {tupla[i]} é um número par')
print(f'o valor 9 apareceu {valor9} vez(es)')
print(f'o valor 3 foi digitado na {posicao + 1}º posição')