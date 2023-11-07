rt_1 = int(input('Informe a primeira reta: '))
rt_2 = int(input('Informe a segunda reta: '))
rt_3 = int(input('Informe a terceira reta: '))

if rt_1 < rt_2 + rt_3 and rt_2 < rt_1 + rt_3 and rt_3 < rt_2 + rt_1:
    print('\nCom essas medidas é possível se formar um triângulo ', end='')
    if rt_1 == rt_2 == rt_3:
        print('EQUILÁTERO.')
    elif rt_1 != rt_2 != rt_3 != rt_1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('\nNão é possível formar um triângulo com tais medidas.')

