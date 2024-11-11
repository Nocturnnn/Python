soma = 0
while True:
    num = float(input('digite um número: [999 para o programa]'))
    if num == 999:
        break
    soma += num
print(f'sua soma é {soma}')