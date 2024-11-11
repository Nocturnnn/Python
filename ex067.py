while True:
    num = float(input('qual o valor da tabuada: '))
    if num < 0:
        break

    i = 1
    while i < 11:
        print(f'{num} * {i} = {num * i:.2f}')
        i += 1
    print('-------------------------------------------------')
print('FIM DO PROGRAMA')