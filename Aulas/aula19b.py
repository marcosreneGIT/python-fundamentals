brasil_0 = []
estado_1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado_2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil_0.append(estado_1)
brasil_0.append(estado_2)

print(brasil_0)
print(brasil_0[0]['sigla'])

estado = dict()
brasil = list()
for i in range(0, 3):
    print()
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print()
for est in brasil:
    for val in est.values():
        print(val, end=' ')
    print()