from random import randint
print('(1) PEDRA')
print('(2) PAPEL')
print('(3) TESOURA')

jogada = int(input('Qual é a sua jogada? '))

computador = randint(1, 3)

print('o computador escolheu {}' .format(computador))
if jogada == 1:
    if computador == 1:
        print('empate')
    elif computador == 2:
        print('computador vence')
    elif computador == 3:
        print('você venceu')
elif jogada == 2:
    if computador == 1:
        print('você venceu')
    elif computador == 2:
        print('empate')
    elif computador == 3:
        print('computador venceu')
elif jogada == 3:
    if computador == 1:
        print('computador venceu')
    elif computador == 2:
        print('você venceu')
    elif computador == 3:
        print('empate')