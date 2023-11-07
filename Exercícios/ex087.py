matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_tc = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um número: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_tc += matriz[l][c]
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
print(f'\nSoma dos números pares: {soma_pares}')
print(f'Soma da terceira coluna: {soma_tc}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')

