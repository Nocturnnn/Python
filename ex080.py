lista = []

for i in range(0, 5):
    n = int(input('digite um valor: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos}')
                break
            pos += 1

print('--=' *30)
print(f'a lista é: {lista}')