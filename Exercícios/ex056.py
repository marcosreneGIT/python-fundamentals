soma_idade = 0
maior_idade_m = 0
m_velho = ''
f_menor_20 = 0
media_idade = 0
for c in range(1, 5):
    print(f'{c}ª PESSOA')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print('')
    soma_idade += idade
    if idade > maior_idade_m and sexo == 'M':
        maior_idade_m = idade
        m_velho = nome
    if idade < 20 and sexo == 'F':
        f_menor_20 += 1
media_idade = soma_idade / 4
print(f'A idade media do grupo é de {media_idade:.1f} anos.')
print(f'O homem mais velho se chama {m_velho} e ele tem {maior_idade_m} anos.')
print(f'O total de mulheres com menos de 20 anos é de {f_menor_20}.')
