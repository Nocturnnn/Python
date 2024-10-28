menu = -1

num1 = float(input('digite um número: '))
num2 = float(input('digite um número: '))

while menu != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos número')
    print('[ 5 ] sair do programa')
    menu = int(input('>>>> qual é sua opção? '))
    print('------------------------------------------------------------')

    if menu == 1:
        print('a soma entre {} e {} é de {}' .format(num1, num2, num1 + num2))
    elif menu == 2:
        print('a soma entre {} e {} é de {}' .format(num1, num2, num1 * num2))
    elif menu == 3:
        if num2 > num1:
            print('{} é maior' .format(num2))
        elif num1 > num2:
            print('{} é maior' .format(num1))
        else:
            print('eles são iguais')
    elif menu == 4:
        num1 = float(input('digite um número: '))
        num2 = float(input('digite um número: '))