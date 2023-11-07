reta_1 = float(input('Informe o comprimento da primeira reta: '))
reta_2 = float(input('informe o comprimento da segunda reta: '))
reta_3 = float(input('Informe o comprimento da terceira reta: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_2 + reta_1:
    print('Com essas medidas é SIM possível se formar um triângulo')
else:
    print('Com essas medidas NÃO é possível se formar um triângulo')
