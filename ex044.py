preco = float(input('qual o preço do produto? R$'))
print('(1) a vista')
print('(2) a vista no cartão')
print('(3) em até 2x no cartão')
print('(4) em até 3x ou mais no cartão')
opcao = int(input('qual opção escolhida? '))

if opcao == 1:
    desconto = preco * (10/100)
    preco = preco - desconto
    print('o valor do produto é de R${:.2f}' .format(preco))
elif opcao == 2:
    desconto = preco * (5/100)
    preco = preco - desconto
    print('o valor do produto é de R${:.2f}' .format(preco))
elif opcao == 3:
    print('o valor do produto é de R${:.2f}' .format(preco))
elif opcao == 4:
    juros = preco * (20/100)
    preco = preco + juros
    print('o valor do produto será de R${:.2f}' .format(preco))
else:
    print('digite uma opção válida, maluco')