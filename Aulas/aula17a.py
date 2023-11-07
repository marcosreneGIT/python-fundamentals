numeros = [1, 2, 5, 7, 2]
numeros[1] = 3
numeros.append(9)
numeros.sort()
print(numeros)
numeros.pop(2)
numeros.insert(3, 8)
if 8 in numeros:
    numeros.remove(8)
else:
    print('O número 8 não esta na lista.')
numeros.sort(reverse=True)
print(numeros)
print(f'Total de elementos: {len(numeros)}')