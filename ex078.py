lista = []
maior = menor = 0
for i in range(0, 5):
    lista.append(int(input('digite um valor: ')))

    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

for i in range(0, len(lista)):
    if lista[i] == maior:
        print(f'o {maior} que é o maior esta na posição {i}')
    if lista[i] == menor:
        print(f'o {menor} que é o menor esta na posição {i}')

#que lindo <3