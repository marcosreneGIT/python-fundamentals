nome_completo = str(input('Digite seu nome completo: ')).strip().split()

print('Seu primeiro nome: {}'.format(nome_completo[0]))
print('Seu ultimo ultimo nome: {}'.format(nome_completo[len(nome_completo) - 1]))
