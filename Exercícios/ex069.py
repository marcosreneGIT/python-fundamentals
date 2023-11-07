mais_18 = 0
homens_quantidade = 0
mulheres_menos_20 = 0
while True:
    sexo = ' '
    continuar_cadastro = ' '
    print('-' * 30, '\n- Cadastro de pessoas -')
    idade = int(input('\nInforme a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais_18 += 1
    if sexo == 'M':
        homens_quantidade += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    while continuar_cadastro not in 'SN':
        continuar_cadastro = str(input('\nDeseja cadastrar mais uma pessoa? [Sim/Não]: ')).strip().upper()[0]
    if continuar_cadastro == 'N':
        break
    print('')
print('-' * 30)
print(f'Total de pessoas maiores de idade: {mais_18}\nTotal de homens: {homens_quantidade}'
      f'\nTotal de mulheres com menos de 20 anos de idade: {mulheres_menos_20}')
