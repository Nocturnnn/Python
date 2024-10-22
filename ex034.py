salario = float(input('digite o salário: '))
aumento = 0

if salario > 1250:
    aumento = salario * (10/100)
elif salario <= 1250:
    aumento = salario * (15/100)

salario = salario + aumento

print('o aumento é de R${} no salario. Salario atual é R${}' .format(aumento,  salario))