primo = int(input('verifique se o número é primo: '))
# começa com um para incluir o valor 1. Pois todo número inteiro é divisivel por 1
indice = 1

for i in range(1, primo + 1):
    if i % primo == 0:
        indice += 1
    print('{}' .format(i), end=' ')
    
#já que todo número é divisivel por 1 e sí mesmo. Então é só contar quantos números esse número é divisivel até chegar nele, so esse quantidade for = ou maior que 3 então o número não é primo
if indice >= 3:
    print('e o {} não é um número primo' .format(primo))
else:
    print('e o {} é um número primo' .format(primo))