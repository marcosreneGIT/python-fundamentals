from math import hypot

cateto_opo = float(input('Informe o comprimento do cateto oposto: '))
cateto_adj = float(input('Informe o comprimento do cateto adjacente: '))
hipo = hypot(cateto_opo, cateto_adj)  # (cateto_opo ** 2 + cateto_adj ** 2) ** (1/2)

print('O tamanho da hipotenusa é referente a: {:.2f}'.format(hipo))
