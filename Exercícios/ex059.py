from time import sleep
pri_val = float(input('Digite um valor: '))
seg_val = float(input('Digite outro valor: '))
menu = True
while menu:
    print('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
    opcao = int(input('\nEscolha uma opção: '))
    if opcao == 1:
        soma = pri_val + seg_val
        print(f'\nSoma:\n{pri_val:.1f} + {seg_val:.1f} = {soma:.1f}')
    elif opcao == 2:
        multi = pri_val * seg_val
        print(f'\nMultiplicação:\n{pri_val:.1f} x {seg_val:.1f} = {multi:.1f}')
    elif opcao == 3:
        print('\nMaior número:')
        if pri_val > seg_val:
            maior_val = pri_val
        else:
            maior_val = seg_val
        print(f'Entre {pri_val:.1f} e {seg_val:.1f} o maior valor é {maior_val:.1f}')
    elif opcao == 4:
        print('\nNovos números')
        pri_val = float(input('Digite novamente o primeiro valor: '))
        seg_val = float(input('Digite novamente o segundo valor: '))
    elif opcao == 5:
        print('\nFinalizando...')
        sleep(2)
        menu = False
    else:
        print('\n\033[31mOpção invalida.\033[m\nTente novamente:')
print('Programa finalizado.')
