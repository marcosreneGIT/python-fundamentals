numeros = [[], []]
numero = 0
for i in range(0, 5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
numeros[0].sort()
numeros[1].sort()
print(f'\nNúmeros pares: {numeros[0]}')
print(f'Números impares: {numeros[1]}')