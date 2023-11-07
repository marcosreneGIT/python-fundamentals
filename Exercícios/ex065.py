continuar_programa = True
contador_numeros = soma = maior_numero = menor_numero = 0
while continuar_programa:
    numeros = int(input('Digite um número: '))
    contador_numeros += 1
    soma += numeros
    continuar_numeros = str(input('Deseja continuar [Sim/Não]: ')).strip().upper()[0]
    print('')
    if continuar_numeros == 'N':
        continuar_programa = False
    elif continuar_numeros not in 'SN':
        print('\n\033[31mOpção invalida.\033[m\n')
    if contador_numeros <= 1:
        maior_numero = menor_numero = numeros
    else:
        if numeros > maior_numero:
            maior_numero = numeros
        elif numeros < menor_numero:
            menor_numero = numeros
media = soma / contador_numeros
print(f'\nTotal de números: {contador_numeros}\nMédia: {media:.2f}\nMaior valor: {maior_numero}'
      f'\nMenor valor: {menor_numero}')
