lista = []
expressao = input('digite sua expressão: ')

for i in expressao:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('sua expressão está válida')
else:
    print('sua expressão está errada')