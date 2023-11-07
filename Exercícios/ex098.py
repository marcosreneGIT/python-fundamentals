from time import sleep


def contador(ini, fin, pas):
    print('\nContador: 1|10|1')
    for i in range(1, 11):
        print(i, end=' ')
        sleep(0.5)
    print('\nContador: 10|0|-2')
    for i in range(10, -1, -2):
        print(i, end=' ')
        sleep(0.5)
    print(f'\nContador: {ini}|{fin}|{pas}')
    for i in range(ini, fin, pas):
        print(i, end=' ')
        sleep(0.5)


inicio = int(input('Informe o inicio da contagem: '))
final = int(input('Informe o final da contagem: '))
passo = int(input('Informe o passo da contagem: '))
if passo == 0:
    passo = 1
contador(inicio, final, passo)
