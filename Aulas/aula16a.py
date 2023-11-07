lanches = ('pizza', 'coxinha', 'pastel')
for i, comer in enumerate(lanches):
    if i < 1:
        print(f'Vou comer {comer}', end='')
    elif 0 < i < len(lanches) - 1:
        print(f', {comer}', end='')
    else:
        print(f' e {comer}')


print('\nComi dimais')

print(lanches)
print(sorted(lanches))
