numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um outro número: ')), int(input('Digite o ultimo número: ')))
print(f'Os valores digitados foram {numeros}')
print(f'Total de vezes em que o número 9 foi digitado: {numeros.count(9)}')
if 3 in numeros:
    print(f'Posição em que aparece o primeiro número 3: {numeros.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados forma: ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
