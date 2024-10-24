frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('essa é a(as) palavra(as) digitada: {}' .format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('a(as) palavra(as) {} é palindromo de {}' .format(junto, inverso))
else:
    print('a(as) palavra(as) {} não é palindromo de {}' .format(junto, inverso))