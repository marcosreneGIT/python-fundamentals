def area(larg, comp):
    ar = larg * comp
    print(f'A área do terreno e de {ar}m2')


print('Controle de área')
largura = float(input('\nInforme a largura: '))
comprimento = float(input('Informe o comprimento: '))
area(largura, comprimento)