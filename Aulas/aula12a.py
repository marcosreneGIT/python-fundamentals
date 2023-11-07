nome = input(str('Digite seu nome: ')).strip().capitalize()

if nome == 'Renê':
    print('Belo nome o seu!')
elif nome == 'Maria' or nome == 'João':
    print('Bem comun o seu nome.')
elif nome in 'Ana Clara Julia':
    print('Um dos mais belos nomes femininos')
else:
    print('Seu nome me chama a atenção.')
print('Prazer em lhe conhecer, \033[97;40;1m{}\033[m'.format(nome))
