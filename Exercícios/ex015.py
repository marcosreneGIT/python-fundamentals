dias_alugados = int(input('Quantos dias o carro foi alugado: '))
km_alugados = float(input('Quantos quilometros foi pecorrido nesse período: '))

valor_aluguel = (dias_alugados*60) + (km_alugados*0.15)

print('\nO valor a ser pago neste período é referente a: R${:.2f}'.format(valor_aluguel))
