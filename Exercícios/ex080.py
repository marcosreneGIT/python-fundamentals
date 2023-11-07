numeros = []
for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        i = 0
        while i < len(numeros):
            if numero <= numeros[i]:
                numeros.insert(i, numero)
                break
            i += 1
print(numeros)
