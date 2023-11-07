numeros = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    while True:
        continuar = str(input('Deseja adcionar mais um número? [S/N]: ')).upper().split()[0]
        if continuar == 'N' or continuar == 'S':
            break
        else:
            print('Opção invalida. Tente novamente.')
    if continuar == 'N':
        break
print(f'\nLista de números: {numeros}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')
