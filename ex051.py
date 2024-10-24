termo1 = int(input('primeiro termo: '))
pregressao = int(input('indice da progressão: '))

for i in range(termo1, termo1 + 10, pregressao):
    print('{}' .format(i), end=' --> ')
print('Acabou negada')