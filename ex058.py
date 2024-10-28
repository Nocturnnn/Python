from random import randint
print('sou seu computador...')
num = randint(0, 10)
print('acabei de pensar em um número entre 0 e 10.')
print('tente adivinhar...')

adivinha = -1
tentativas = 0

while num != adivinha:
    tentativas += 1
    adivinha = int(input('qual seu palpite? '))
    
    if adivinha > num:
        print('menos... tente mais uma vez.')
    elif adivinha < num:
        print('mais... tente mais uma vez.')

print('parabéns!!! você acertou com {} tentativas.' .format(tentativas))