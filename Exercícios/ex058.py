from random import randint
print('''Olá, sou seu computador e será um prazer jogar este jogo com o senhor.\nEstou pensando em um número de 0 a 10.
Você agora terá quantas tentativas precisar.''')
chut_pc = randint(0, 10)
chut_p1 = int(input('\nTente o adivinhar: '))
tent_p1 = 1
while chut_p1 != chut_pc:
    tent_p1 += 1
    if chut_p1 > chut_pc:
        chut_p1 = int(input('\nUm pouco alto.\nTente algo menor: '))
    else:
        chut_p1 = int(input('\nUm pouco baixo.\nTente algo maior: '))
print(f'\nVocê acertou, parabéns!\nLevou apenas {tent_p1} tentativas para chegar ao resultado, incrível.')
