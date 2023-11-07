from time import sleep


def maior(*num):
    maior_valor = 0
    for val in num:
        print(val, end=' ')
        sleep(0.3)
        if val > maior_valor:
            maior_valor = val
    print(f'\nO total de números forma: {len(num)}')
    print(f'O maior valor foi: {maior_valor}\n')


maior()
maior(1, 4, 5, 6, 7)
maior(-3, 0, -1)

