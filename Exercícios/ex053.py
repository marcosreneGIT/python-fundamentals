frase = str(input('Digite uma frase: ')).strip().upper().split()
frase_junta = ''.join(frase)
frase_invertida = ''
for i in range(len(frase_junta) - 1, -1, -1):
    frase_invertida += frase_junta[i]
print('O inverso de {} é igual a {}.'.format(frase_junta, frase_invertida))
if frase_junta == frase_invertida:
    print('Temos um palíndromo.')
else:
    print('Não se trata de um palíndromo.')
