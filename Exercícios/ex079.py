numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
    else:
        print('\nEste número já foi adicionado.')
    while True:
        continuar_numeros = str(input('\nDeseja adcionar mais um valor? [SIM/NÃO]: ')).upper().split()[0]
        if continuar_numeros == 'S' or continuar_numeros == 'N':
            break
        else:
            print('Opção invalida.')
    if continuar_numeros == 'N':
        break
print(sorted(numeros))
