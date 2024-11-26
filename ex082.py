lista = []
listaPar = []
listaImpar = []

while True:
    num = int(input('digite um número: '))
    lista.append(num)

    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    
    continuar = str(input('quer continuar?[S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'toda lista: {lista}')
print(f'números pares: {listaPar}')
print(f'números impares: {listaImpar}')