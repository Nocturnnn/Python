soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        cont += 1
print('a soma de todos os {} valores é {}' .format(cont, soma))