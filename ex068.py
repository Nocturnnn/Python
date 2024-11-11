print('VAMOS JOGAR PAR OU IMPAR')
par = impar = False
import random

while True:
    valor = int(input('digite um valor: '))
    pi = str(input('Par ou Impar? [P/I]')).upper().strip()[0]

    computador = random.randint(0, 10)
    
    soma = valor
    soma += computador
    print(f'{valor} + {computador} = {soma}')

    if soma % 2 == 0:
        par = True
    else:
        impar = True

    if par == True and pi == 'P' or impar == True and pi == 'I':
        print('Parabens você ganhou!!!!')
    else:
        break
print('Você perdeu!!!!')