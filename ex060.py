fatorial = int(input('digite o número para o cálculo de fatorial: '))
i = fatorial

while i != 1:
    i -= 1
    fatorial *= i
print('seu número fatorial é {}' .format(fatorial))