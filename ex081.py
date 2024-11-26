lista = []
i = 0
valor5 = False

while True:
    lista.append(int(input('digite um valor: ')))
    continuar = str(input('quer continuar?[S/N] ')).upper().strip()[0]

    i += 1

    for cont in range(0, len(lista)):
        if lista[cont] == 5:
            valor5 = True

    if continuar == 'N':
        break

lista.sort(reverse=True)

print('--=' *30)

print(lista)

if valor5 == True:
    print('o valor 5 foi digitado')
else:
    print('o valor 5 não foi digitado')