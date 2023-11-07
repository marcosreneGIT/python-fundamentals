palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM')
for palavra in palavras:
    print(f'A palavra {palavra:20} Possui as vogais: ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')
    print()




