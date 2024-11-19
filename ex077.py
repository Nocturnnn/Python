palavras = ('aprender', 'programar', 'linguagem', 'python')
print(f'palavra que seram verificada se tem vogais --> {palavras}| ')

for i in range(0, len(palavras)):
    print(f'|{palavras[i]}| tem essas vogais -->')
    for cadaletra in range (0, len(palavras[i])):
        letra = palavras[i]

        if letra[cadaletra] == 'a':
            print('a ', end='')
        elif letra[cadaletra] == 'e':
            print('e ', end='')
        elif letra[cadaletra] == 'i':
            print('i ', end='')
        elif letra[cadaletra] == 'o':
            print('o ', end='')
        elif letra[cadaletra] == 'u':
            print('u ', end='')
    i += 1