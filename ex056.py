contagemDeFemea = 0

media = 0
soma = 0

velho = 0
nomeDoVelho = ''

for i in range(1, 5):
    nome = str(input('qual o nome da {} pessoa? ' .format(i)))
    idade = int(input('qual a idade da {} pessoa? ' .format(i)))
    sexo = str(input('qual o sexo da {} pessoa? digite M para masculino e F para feminino: ' .format(i))).upper().strip()
    print('-------------------------------------------------------------')

    soma = soma + idade

    if i == 1:
        velho = idade
    else:
        if idade > velho:
            velho = idade
            nomeDoVelho = nome

    if sexo == 'F':
        contagemDeFemea += 1

media = soma / 4

print('a media de idade entre essas pessoas é de {}' .format(media))
print('o nome da pessoa mais velha é {}' .format(nomeDoVelho))
print('o número de mulheres é {}' .format(contagemDeFemea))