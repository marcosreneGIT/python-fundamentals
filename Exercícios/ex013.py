sal = float(input('Informe o salário do funcionário: R$'))
novo_sal = sal + (sal * 15 / 100)

print('Com base no valor R${:.2f} o novo reajuste de 15% fara com que salário chegue a R${:.2f}'.format(sal, novo_sal))



