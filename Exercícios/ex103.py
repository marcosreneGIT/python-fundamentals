def ficha(nome_j='desconhecido', qunt_g=0):
    print(f'\nO jogador {nome_j} fez {qunt_g} gol(s).')


nome_jogador = str(input('Informe o nome do jogador: '))
gols_jogador = str(input('Informe o total de gols deste jogador: '))
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador.strip() == '':
    ficha(qunt_g=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)
