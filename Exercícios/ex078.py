numeros = []
maior = 0
menor = 0
for i in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
    maior = max(numeros)
    menor = min(numeros)
print(f'Os números digitados foram: {numeros}')
print(f'Maior número: {maior}\nMenor número: {menor}')
print('Posição do(s) maior(es) número(s): ', end='')
for i, numero in enumerate(numeros):
    if numero == maior:
        print(i + 1, end='. ')
print('\nPosição do(s) menor(es) número(s): ',end='')
for i, numero in enumerate(numeros):
    if numero == menor:
        print(i + 1, end='. ')
