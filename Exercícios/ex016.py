from math import trunc

num = float(input('Digite um número: '))

print('O número digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
print('O número digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
print('O número digitado foi {} e a sua porção inteira é {:.0f}'.format(num, num))

