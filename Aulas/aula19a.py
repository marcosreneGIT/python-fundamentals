pessoa = {'nome': 'Marcos', 'idade': 19, 'sexo': 'M'}
print(pessoa['nome'])
print(f'{pessoa["nome"]} do sexo {pessoa["sexo"]} tem {pessoa["idade"]} anos.')


print('\n', pessoa.keys())
for k in pessoa.keys():
    print(k)

print('\n', pessoa.values())
for v in pessoa.values():
    print(v)

print('\n', pessoa.items())
for k, v in pessoa.items():
    print(k, ':', v)


del pessoa['sexo']
pessoa['nome'] = 'Clara'
pessoa['peso'] = 60.0
print('\n', pessoa)