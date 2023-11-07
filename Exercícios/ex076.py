listagem_produtos = ('Lápis', 2.15, 'Borracha', 0.85, 'Caderno', 15.90,
                     'Estojo', 5.50, 'Mochila', 87.90, 'Régua', 6.00)
print('Lista de produtos: ')
for i in range(0, len(listagem_produtos)):
    if i % 2 == 0:
        print(f'{listagem_produtos[i]:10}....................   R$', end='')
    else:
        print(f'{listagem_produtos[i]:.2f}')
print('-'*40)
