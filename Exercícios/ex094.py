pessoas = list()
dados = dict()
soma_idade = 0
while True:
    dados['nome'] = str(input('Informe o nome: ')).strip().capitalize()
    while True:
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            dados['sexo'] = sexo
            break
        else:
            print('\nOpção invalida! Digite apenas "M" ou "F"\n')
    dados['idade'] = int(input('Informe a idade: '))
    soma_idade += dados['idade']
    pessoas.append(dados.copy())
    while True:
        continuar = str(input('\nDeseja cadastrar mais uma pessoa? [S/N]: ')).upper()
        if continuar == 'N' or continuar == 'S':
            break
        else:
            print('\nOpção invalida! Digite apenas "S" ou "N"\n')
    if continuar == 'N':
        break
print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')
media_idade = soma_idade / len(pessoas)
print(f'Media de idade: {media_idade:.2f}')
print('\nLista de mulheres: ')
for dados in pessoas:
    if dados['sexo'] in 'F':
        print(f'- {dados["nome"]}')
print('\nPessoas a cima da media em idade: ')
for dados in pessoas:
    if dados['idade'] > media_idade:
        print(f'Nome: {dados["nome"]} |Sexo: {dados["sexo"]} |Idade: {dados["idade"]}')
        print()