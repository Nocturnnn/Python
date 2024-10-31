novenovenove = 999
cont = 0
num = 0

while novenovenove != 0:
    numPassado = num
    num = int(input('digite um número [999 é condição de parada]: '))
    cont += 1
    arm = 0

    if num == novenovenove:
        # para parar o loop
        novenovenove = 0
        # para rodar só quanto a condição de parada for atingida
        arm = 999

    num += numPassado
    if arm == 999:
        # para desconciderar a condição de parada
        num -= 999
        cont -= 1

        print('foram somados {} números e o resultado é {}' .format(cont, num))