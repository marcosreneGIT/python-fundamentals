km_viagem = float(input('Informe a distância da sua viagem: '))

preco = km_viagem * 0.50 if km_viagem <= 200 else km_viagem * 0.45
print('A viagem ficará R${:.2f}'.format(preco))
