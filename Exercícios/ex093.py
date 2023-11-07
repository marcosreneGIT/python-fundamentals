jogador = dict()
gols = list()
quant_gols = 0
jogador['nome'] = str(input('Nome do jogador: '))
n_partidadas = int(input(f'Quantas partidadas {jogador["nome"]} fez: '))
for i in range(0, n_partidadas):
    gol = int(input(f' - Quantidade de gols na {i+1}⁰ partida: '))
    quant_gols += gol
    gols.append(gol)
jogador['gols'] = gols[:]
jogador['quantidade'] = quant_gols
print(f'\nDados do jogador {jogador["nome"]} nas ultimas {n_partidadas} partidads')
for i, g in enumerate(jogador['gols']):
    print(f'Na {i+1}⁰ partida total de: {g} gol')
print(f'Total de {jogador["quantidade"]} gols em {n_partidadas} partidas')

