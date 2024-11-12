contSexoM = 0
contIdade = 0
contSexoIdadeF = 0

while True:
    idade = int(input('informe sua idade: '))
    sexo = str(input('informe seu sexo: [M/F]')).upper().strip()[0]

    if idade >= 18:
        contIdade += 1
    
    if sexo == 'M':
        contSexoM += 1

    if sexo == 'F' and idade < 20:
        contSexoIdadeF += 1

    print('----------------------------------------------')
    continuar = str(input('quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        print('-----------------------------------------------')
        print(f'Há {contIdade} pessoas com mais de 18 anos')
        print(f'Há {contSexoM} homens cadastrados')
        print(f'existe {contSexoIdadeF} mulheres com menos de 20 anos')
        break
