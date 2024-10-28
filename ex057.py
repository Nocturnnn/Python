i = 1
while i != 0:
    sexo = str(input('informe seu sexo [F/M]: ')).upper().strip()
    if sexo == 'M' or sexo == 'F':
        print('sexo {} registrado com sucesso!!!!' .format(sexo))

        # para encerrar o laço
        i = 0
    else:
        print('dados inválidos por favor digite [F/M]!!!')