largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))

area_quadrada = (largura * altura)
tinta_nescessaria = (area_quadrada / 2)

print('\nCom {}m de largura e {:.2f}m de altura você tera uma área de {:.2f}m2'.format(largura, altura, area_quadrada))
print('Sendo assim será um total de {:.3f}l de tita para a pintura'.format(tinta_nescessaria))
