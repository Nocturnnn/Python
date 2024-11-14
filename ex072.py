numE = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorse', 'quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')

num = 0
while True:
    num = int(input('digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'seu número por extenso é {numE[num]}')
    else:
        break
print('digite um número entre 0 e 20')