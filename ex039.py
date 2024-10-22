ano = int(input('digite o ano de seu nascimento: '))

idade = 2024 - ano
alistamento = ano + 18

print('quem nasceu em {} tem {} anos em 2024' .format(ano, idade))

if idade > 18:
    print('você já deveria ter se alistado há {} anos' .format(idade - 18))
    print('seu alistamento foi em {}' .format(alistamento))
elif idade == 18:
    print('aliste agora noia')
    print('seu alistamento é esse ano')
else:
    print('você deve se alistar em {} anos' .format(18 - idade))
    print('seu alistamento sera em {}' .format(alistamento))