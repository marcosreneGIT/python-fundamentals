from random import randint
contador_vitorias = 0
while True:
    jogada_pc = randint(1, 10)
    jogada_p1 = int(input('Digite um número: '))
    ecolha_par_impar = str(input('Você escolher [PAR] ou [IMPAR]: ')).strip().upper()[0]
    soma = jogada_pc + jogada_p1
    print(f'\nVocê escolheu o número: {jogada_p1} \nO computador escolheu o número: {jogada_pc}\nO total é de: {soma}')
    print('Resultado: PAR' if soma % 2 == 0 else 'Resultado: ÍMPAR\n')
    if ecolha_par_impar == 'P':
        print('Você escolheu par e o computador ficou com impar.')
        if soma % 2 == 0:
            print('\nVocê venceu!\nVamos jogar novamente...\n')
            contador_vitorias += 1
        else:
            print('Fim de jogo.\nVocê perdeu.')
            break
    elif ecolha_par_impar == 'I':
        print('Você escolheu impar e o computador ficou com par.')
        if soma % 2 != 0:
            print('\nVocê venceu!\nVamos jogar novamente...\n')
            contador_vitorias += 1
        else:
            print('Fim de jogo.\nVocê perdeu.')
            break
    else:
        print('\n\033[31mOPÇÃO INVALIDA.\033[m\n')
print(f'\nVocê ganhou um total de {contador_vitorias} vezes do computador.')
