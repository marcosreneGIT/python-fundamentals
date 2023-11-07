def fatorial(num, show):
    """
     - função responsavel por mostrar a fatorial de um número.
    :param num: número para se saber a fatorial.
    :param show: escolha logica para se saber se retorna o processo de resolução da fatorial ou não.
    :return: resultado da fatorial.
    """
    from time import sleep
    fat = 1
    print(f'\nFatorial de {num}! =', end=' ')
    for c in range(num, 0, -1):
        if show:
            if c != 1:
                print(c, end=' x ')
                sleep(0.4)
            else:
                print(c, '= ', end='')
                sleep(0.4)
        fat *= c
    return fat


mostrar_processo = True
numero_fatorial = int(input('Digite o número que deseja saber a fatorial: '))
while True:
    opcao_mostrar_processo = str(input('Deseja mostrar o processo da fatorial? [S/N]: ')).upper().strip()
    if opcao_mostrar_processo not in 'SN':
        print('\nOpção invalida. Digite apenas "S" ou "N".\n')
    else:
        if opcao_mostrar_processo == 'S':
            break
        elif opcao_mostrar_processo == 'N':
            mostrar_processo = False
            break
print(fatorial(numero_fatorial, mostrar_processo))
