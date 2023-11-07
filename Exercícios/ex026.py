frase = str(input('Digite uma frase: ')).strip().upper()

print('Quantidade de letras A: {}'.format(frase.count('A')))
print('Posição da primeira letra A: {}'.format(frase.find('A') + 1))
print('Posição da ultima letra A: {}'.format(frase.rfind('A') + 1 - frase.count(' ')))

