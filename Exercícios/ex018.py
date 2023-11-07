import math

angulo = float(input('Iforme o ângulo: '))

seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Seno: {:.2f}\nCoseno: {:.2f}\nTangete: {:.2f}'.format(seno, coseno, tangente))


