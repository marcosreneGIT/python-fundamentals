from random import randint
numeros = (randint(0, 9), randint(0, 9), randint(0, 9),
           randint(0, 9), randint(0, 9))
maior_numero = 0
menor_numero = 0
for i, numero in enumerate(numeros):
    print(numero, end=' ')
    if i == 0:
        maior_numero = numeros[0]
        menor_numero = numeros[0]
    else:
        if numeros[i] > maior_numero:
            maior_numero = numeros[i]
        if numeros[i] < menor_numero:
            menor_numero = numeros[i]
print(f'\nMaior número: {maior_numero}\nMenor número: {menor_numero}')
print(f'\nMaior número: {max(numeros)}\nMenor número: {min(numeros)}')


