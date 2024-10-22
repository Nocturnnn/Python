print('emprestimo bancário')
casa = float(input('qual o valor da casa? '))
salario = float(input('qual o salário do comprador? '))
anos = float(input('em quantos anos o comprador vai parcelar? '))

mes = anos * 12
parcela = casa / mes
porcentoSalario = salario * (30/100)

if porcentoSalario < parcela:
    print('emprestimo negado')
else:
    print('emprestimo aprovado')