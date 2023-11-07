numeros = []
for i in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
for i, numero in enumerate(numeros):
    print(f'Na posição {i + 1} encontrei o número {numero}')
