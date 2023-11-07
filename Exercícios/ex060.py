numero = int(input('Digite um número: '))
c = numero
fatorial = 1
print(f'\n{numero}! =', end=' ')
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    fatorial = fatorial * c
    c -= 1
print(fatorial)

print('')

fat = 1
print(f'{numero}! =', end=' ')
for c in range(numero, 0, -1):
    fat = fat * c
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
print(fat)
