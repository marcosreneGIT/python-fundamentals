lista_passagem = []
lista = []
maior_peso = menor_peso = 0
while True:
    lista_passagem.clear()
    lista_passagem.append(str(input('Informe seu nome: ')))
    lista_passagem.append(float(input('Iforme seu peso (kg): ')))
    lista.append(lista_passagem[:])
    if len(lista) == 1:
        maior_peso = menor_peso = lista_passagem[1]
    else:
        if lista_passagem[1] >= maior_peso:
            maior_peso = lista_passagem[1]
        if lista_passagem[1] <= menor_peso:
            menor_peso = lista_passagem[1]
    while True:
        resposta = str(input('\nDeseja continuar? [SIM/NÃO]: ')).upper().strip()[0]
        print()
        if resposta == 'S' or resposta == 'N':
            break
        else:
            print('Opção invalida. Tente novamente.')
    if resposta == 'N':
        break
print(f'Quantidade de pessoas cadastradas: {len(lista)}')
print('Pessoas mais pesadas: ', end='')
for pessoa in lista:
    if pessoa[1] == maior_peso:
        print(pessoa[0], end='. ')
print(f'({maior_peso}kg)')
print('Pessoas mais leves: ', end='')
for pessoa in lista:
    if pessoa[1] == menor_peso:
        print(pessoa[0], end='. ')
print(f'({menor_peso}kg)')
