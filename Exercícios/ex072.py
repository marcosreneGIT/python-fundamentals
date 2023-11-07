numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
while True:
    numero = int(input('Digite um número entre 0 a 5: '))
    if 0 <= numero <= 5:
        print(f'Você digitou o número {numeros[numero]}.')
        continuar_numeros = ' '
        while continuar_numeros not in 'SN':
            continuar_numeros = str(input('\nDeseja saber mais algum número [SIM/NÃO]: ')).strip().upper()[0]
        if continuar_numeros == 'N':
            break
    else:
        print('O número deve estar entre 0 e 5.\nTente novamente.\n')
