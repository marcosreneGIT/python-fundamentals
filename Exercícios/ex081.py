lista_numeros = []
while True:
    lista_numeros.append(int(int(input('Digite um número: '))))
    while True:
        continuar_numeros = str(input('Deseja adcionar mais um valor? [SIM/NÃO]: ')).upper().split()[0]
        if continuar_numeros == 'S' or continuar_numeros == 'N':
            break
        else:
            print('Opção invalida. Tente novamente.\n')
    print()
    if continuar_numeros == 'N':
        break
lista_numeros.sort(reverse=True)
print(f'Quantidade de números digitados: {len(lista_numeros)}')
print(f'Lista ordenada de forma decrescente: {lista_numeros}')
print('O valor 5 foi digitado: ', end='')
if 5 in lista_numeros:
    print('SIM')
else:
    print('NÃO')

