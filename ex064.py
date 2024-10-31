SouN = 'S'
num = media = cont = somaPassada = maior = menor = 0

while SouN != 'N':
    somaPassada = num
    menor = num
    num = float(input('digite um número: '))
    SouN = str(input('quer continuar? [S/N] ')).upper().strip()
    cont += 1

    somaPassada += num

    if SouN == 'S':
        media = num / cont

    maior = num
    if menor > maior:
        maior = menor