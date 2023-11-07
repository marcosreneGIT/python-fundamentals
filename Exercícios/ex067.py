tabuada = True
while tabuada:
    multiplicador_tabuada = 1
    numero_tabuda = int(input('Informe um número para saber sua tabuada: '))
    if numero_tabuda < 0:
        break
    print('-' * 12)
    while multiplicador_tabuada <= 10:
        produto_tabuada = numero_tabuda * multiplicador_tabuada
        print(f'{numero_tabuda} x {multiplicador_tabuada} = {produto_tabuada}')
        multiplicador_tabuada += 1
    print('-' * 12)
    continuar_tabuada = ' '
    while continuar_tabuada not in 'SN':
        continuar_tabuada = str(input('Deseja saber a tabuada de mais algum número [Sim/Não]: ')).strip().upper()[0]
        if continuar_tabuada == 'N':
            tabuada = False
        elif continuar_tabuada not in 'SN':
            print('\n\033[31mOpçao invalida.\033[m')
print('Programa finalizado.')


