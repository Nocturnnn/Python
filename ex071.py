saque = int(input('qual o valor do saque? '))
num = saque

num50 = num20 = num1 = 0

while True:
    if num >= 100:
        num -= 50

        num50 += 1
    elif num < 100 and num >= 20:
        num -= 20

        num20 += 1
    elif num < 20 and num > 0:
        num -= 1

        num1 += 1
    elif num == 0:
        break

print(f'{num50} cédulas de R$50')
print(f'{num20} cédulas de R$20')
print(f'{num1} cédulas de R$1')