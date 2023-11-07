from random import randint
from time import sleep
jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)}
ranking = list()
print('Resultados: ')
for k, v in jogo.items():
    print(f'- {k}: {v}')
    sleep(1.5)
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
print('\nRanking: ')
for i, e in enumerate(ranking):
    print(f'- {i+1} {e[0]}: {e[1]}')
    sleep(0.5)
