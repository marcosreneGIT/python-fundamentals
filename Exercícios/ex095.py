jogador = dict()
time = list()
gol = list()
while True:
    jogador['nome'] = str(input('\nInforme o nome do jogador: ')).strip().capitalize()
    numero_partidas = int(input(f'Informe o total de partidas que o jogador {jogador["nome"]} atuou: '))
    print()
    for i in range(0, numero_partidas):
        gol.append(int(input(f'Informe a quantidade de gols na {i+1}° partida: ')))
    jogador['gols'] = gol[:]
    time.append(jogador.copy())
    gol.clear()
    jogador.clear()
    while True:
        continuar_cadastro = str(input('\nDeseja cadastrar mais algum jogador? [S/N]: ')).strip().upper()
        if continuar_cadastro == 'S' or continuar_cadastro == 'N':
            break
        else:
            print('\nOpção invalida! Digite apenas "S" ou "N".')
    if continuar_cadastro == 'N':
        break
print('\nCódigo | Nome | Gols | Total de gols:\n')
for i, jogador in enumerate(time):
    print(f' {i} | {jogador["nome"]} | {jogador["gols"]} | {sum(jogador["gols"])}')
while True:
    opcao_jogador = int(input('\nInforme o codigo do jogar que deseja saber mais informações [-1 para sair]: '))
    if opcao_jogador >= len(time):
        print('\nCódigo invalido! jogador não encontrado.')
    elif opcao_jogador == -1:
        break
    else:
        print(f'\nDados do jogador {time[opcao_jogador]["nome"]}: ')
        for i, gol in enumerate(time[opcao_jogador]['gols']):
            print(f'No {i+1}° jogo ele fez {gol} gols.')
