from random import randint
from time import sleep
numeros = list()


def sorteio(lista):
    print('Números sorteados: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
        sleep(0.4)


def soma_par(lista):
    soma_p = 0
    print('\nSoma dos pares: ', end='')
    for val in lista:
        if val % 2 == 0:
            soma_p += val
    print(soma_p)


sorteio(numeros)
soma_par(numeros)
