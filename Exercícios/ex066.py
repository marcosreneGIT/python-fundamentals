soma = contador_numeros = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    contador_numeros += 1
print(f'\nSoma: {soma}\nTotal de números: {contador_numeros}')