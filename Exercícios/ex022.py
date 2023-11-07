nome_completo = input('Digite seu nome completo: ').strip()

print('Nome com todas as letras maiúsculas: {}'.format(nome_completo.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome_completo.lower()))
print('Quantidade de letras no seu nome: {}'.format(len(nome_completo) - nome_completo.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(nome_completo.find(' ')))

# letras_nome_1 = nome_completo.split()
# print('Seu primeiro nome é {} e possui {} letras'.format(letras_nome_1[0], len(letras_nome_1[0])))


