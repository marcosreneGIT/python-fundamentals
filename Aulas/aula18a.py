pessoa= []
pessoa.append('Marcos')
pessoa.append(19)
grupo = []
grupo.append(pessoa[:])
pessoa[0] = 'Renê'
pessoa[1] = 91
grupo.append(pessoa[:])
print(grupo)
print()
grupo = [['Marcos', 19], ['Renê', 91]]
for pessoas in grupo:
    print(f'Idade de {pessoas[0]}: {pessoas[1]}')
print()
registro = []
dados = []
for i in range(0, 2):
    dados.append(str(input('Seu nome: ')))
    dados.append(int(input('Sua idade: ')))
    registro.append(dados[:])
    dados.clear()
print()
for dado in registro:
    print(f'Idade de {dado[0]}: {dado[1]}')
