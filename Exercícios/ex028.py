from random import randint

numero_aleatorio = randint(0, 5)

chute = int(input('De 0 a 5 tente acertar o número que estou pensando: '))

print('Você chutou {} e eu estava pensando em {}'.format(chute, numero_aleatorio))
if chute == numero_aleatorio:
    print('Nossa você acertou.')
else:
    print('Tente ser melhor na proxima.')



