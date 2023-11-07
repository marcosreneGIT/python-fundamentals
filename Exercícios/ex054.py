from datetime import date
ano_atual = date.today().year
cont_maior = 0
cont_menor = 0
for c in range(1, 8):
    nasc = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = ano_atual - nasc
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print('\nPessoas maiores de idade: {}\nPessoas menores de idade: {}'.format(cont_maior, cont_menor))
