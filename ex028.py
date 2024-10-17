import random
print('vou pensar em um número entre 1 e 5 tente adivinhar...')
numAdivinhado = random.randint(1,5)

numJogador = int(input('qual número eu pensei? '))
if numAdivinhado == numJogador:
    print('Parabéns seu verme, você ganhou o número é {}' .format(numAdivinhado))
else:
    print('Patetico!! você errou eu pensei no {}' .format(numAdivinhado))