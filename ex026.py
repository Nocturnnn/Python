frase = str(input('digite uma frase: ')).upper().strip()
print('a letra A aparece {} vezes na frase' .format(frase.count('A')))
print('a primeira que letra A aparece na posição {}' .format(frase.find('A')+1))
print('a ultima posição que a letra A aparece é na posição {}' .format(frase.rfind('A')+1))