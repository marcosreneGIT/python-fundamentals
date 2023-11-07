listas = [[], [], []]
for i_l in range(0, 3):
    for i in range(0, 3):
        numero = int(input('Digite um número: '))
        listas[i_l].append(numero)
for l in range(0, 3):
    for i in range(0, 3):
        print(f'[{listas[l][i]}]', end=' ')
    print()
