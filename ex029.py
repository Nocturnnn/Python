vel = float(input('qual a velocidade atual do carro? '))

if vel <= 40 and vel > 0:
    print('muito devagar acelera essa lata velha!!!')
elif vel >= 41 and vel <= 80:
    print('você é uma pessoa normal na sua vida normal com seu carro normal tendo sua vida normal')
else:
    multa = (vel - 80) * 7
    print('tá achando que você é o braian, quer ficar a 4 paumos abaixo da terra? sua multa é de {:.2f}R$' .format(multa))