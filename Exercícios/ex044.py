print('-' * 8, 'Loja Marculino Modas', '-' * 8)
preco_total = float(input('Informe o valor total das compras: R$'))
print('''[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em ate 2X no cartão: Preço normal
[4] 3X ou mais no cartão: 20% de juros''')
metodo_pagamento = int(input('Escolha o metodo de pagamento: '))
print()

if metodo_pagamento == 1:
    metodo_1 = preco_total - (preco_total * 0.10)
    print('O valor de R${:.2f} deverá ser pago a vista em dinheiro ou cheque.'.format(metodo_1))
elif metodo_pagamento == 2:
    metodo_2 = preco_total - (preco_total * 0.05)
    print('O valor de R${:.2f} deverá ser pago a vista no cartão.'.format(metodo_2))
elif metodo_pagamento == 3:
    metodo_3 = preco_total / 2
    print('O valor de R${:.2f} deverá ser pago 2X no cartão.'.format(metodo_3))
elif metodo_pagamento == 4:
    parcelas = int(input('Informe a quantidade de parcelas que deseja: '))
    metodo_4 = (preco_total + (preco_total * 0.20)) / parcelas
    print('O valor de R${:.2f} deverá ser pago {}X no cartão.'.format(metodo_4, parcelas))
else:
    print('\033[31mOPÇÃO INVALIDA')
print('\nFim do programa')