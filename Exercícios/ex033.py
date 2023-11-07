numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
numero_3 = int(input('Digite outro número: '))
maior_valor = numero_1
menor_valor = numero_1

if numero_2 > maior_valor:
    maior_valor = numero_2
if numero_3 > maior_valor:
    maior_valor = numero_3

if numero_2 < menor_valor:
    menor_valor = numero_2
if numero_3 < menor_valor:
    menor_valor = numero_3

print('Maior valor: {}'.format(maior_valor))
print('Menor valor: {}'.format(menor_valor))
