n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))

lista = [n1, n2, n3, n4]

import random
escolhido1 = random.choice(lista)
print('o primeiro aluno escolhido é {}' .format(escolhido1))

lista.remove(escolhido1)
escolhido2 = random.choice(lista)
print('o segundo aluno escolhido é {}' .format(escolhido2))

lista.remove(escolhido2)
escolhido3 = random.choice(lista)
print('o terceiro aluno escolhido é {}' .format(escolhido3))

lista.remove(escolhido3)
escolhido4 = random.choice(lista)
print('o quarto aluno escolhido é {}' .format(escolhido4))