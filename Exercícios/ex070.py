total_compra = maior_mil = contador = menor_preco = 0
nome_menor_preco = ' '
while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip().capitalize()
    preco_produto = float(input('Informe o valor do produto: R$'))
    total_compra += preco_produto
    contador += 1
    if preco_produto > 1000:
        maior_mil += 1
    if contador == 1 or preco_produto < menor_preco:
        menor_preco = preco_produto
        nome_menor_preco = nome_produto
    continuar_cadastro = ' '
    while continuar_cadastro not in 'SN':
        continuar_cadastro = str(input('Deseja continuar [Sim/Não]: ')).upper().strip()[0]
    print('')
    if continuar_cadastro == 'N':
        break
print(f'Total gasto: R${total_compra:.2f}\nTotal de produtos acima de R$1000.00: {maior_mil}'
      f'\nNome do produto mais barato: {nome_menor_preco}')
