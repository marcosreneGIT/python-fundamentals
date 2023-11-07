from random import randint
from time import sleep
numeros = []
jogos = []
contador_numeros = contador_jogos = 0
quantidade_jogos = int(input('Digite a quantidade de jogos: '))
while contador_jogos < quantidade_jogos:
    numeros.clear()
    contador_numeros = 0
    while contador_numeros < 6:
        numero = randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
            contador_numeros += 1
    jogos.append(numeros[:])
    contador_jogos += 1
for numero_jogo, listas in enumerate(jogos):
    listas.sort()
    print(f'Jogo {numero_jogo + 1}: {listas}')
    sleep(2)
