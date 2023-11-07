casa_val = float(input('Informe o valor da casa: R$'))
sal = float(input('Informe o valor do seu salário: R$'))
anos = int(input('Informe a quantidade de anos que deseja financiar: '))
mens = casa_val / (anos * 12)

print('\nDeseja financiar um casa no valor de R${:.2f} '
      'tendo uma renda mensal de R${:.2f}'.format(casa_val, sal))
print('Sendo assim você teria uma mensalidade de R${:.2f} em {} anos.\n'.format(mens, anos))

if mens > (sal * 0.30):
    print('Com os valores apresentados não é possivel o financiamento.\n\033[1;31mNEGADO')
else:
    print('Com os valores apresentados será um prazer realizar o financiamento.\n\033[1;32mAPROVADO')
