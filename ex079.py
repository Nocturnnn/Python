lista = []
while True:
    num = int(input('digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('valor duplicado, digite um valor diferente...')
    continuar = str(input('quer continuar?[S/N] ')).upper().strip()[0]

    if continuar == 'N':
        break

lista.sort()
print(f'sua lista: {lista}')