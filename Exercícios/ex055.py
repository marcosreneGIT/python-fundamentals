maior_peso = 0
menor_peso = 0
for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print('\nMaior peso: {:.1f}Kg\nMenor peso: {:.1f}Kg'.format(maior_peso, menor_peso))
