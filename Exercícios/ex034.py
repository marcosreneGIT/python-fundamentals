print('Caso seja salário mínimo (R$1320) aperte [0]')
salario = float(input('Informe seu salário: '))
minimo_salario = 1320
novo_salario = 0
aumento_15 = salario * 0.15
aumento_10 = salario * 0.10

if salario == 0:
    novo_salario = minimo_salario + (minimo_salario * 0.10)
elif salario <= 1250:
    novo_salario = salario + aumento_15
else:
    novo_salario = salario + aumento_10
print('Com o reajuste proporcional seu salário ficara em R${:.2f}'.format(novo_salario))

