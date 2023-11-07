preco = float(input('Informe o valor do produto: R$'))
preco_desconto = preco - (preco * 5) / 100

print('O produto que antes era R${:.2f} com o desconto de 5% passou a ser R${:.2f}'.format(preco, preco_desconto))
