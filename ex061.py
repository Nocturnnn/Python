primeiro = int(input('digite o primeiro termo: '))
rasao = int(input('digite a razão do PA: '))

cont = 0
i = 0
while i < 10:
    print('{} --> ' .format(primeiro), end='')
    primeiro += rasao
    i += 1
    cont += 1

if i == 10:
    aMais = int(input('quantos termos você quer mostrar a mais? '))
    contadorDoAMais = aMais
    while contadorDoAMais > 0:
        print('{} --> ' .format(primeiro), end='')
        primeiro += rasao
        cont += 1
        contadorDoAMais -= 1
        if contadorDoAMais == 0:
            aMais = int(input('quantos termos você quer mostrar a mais? '))
            contadorDoAMais = aMais
            if aMais == 0:
                print('progressão finalizada com {} termos mostrados.' .format(cont))