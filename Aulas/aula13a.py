inic = int(input('Informe o início: '))
fim = int(input('Informe o final: '))
pulo = int(input('Informe o tamanho do passo: '))
for c in range(inic, fim + 1, pulo):
    print(c)
print('\nDe {} a {} pulando de {} em {}'.format(inic, fim, pulo, pulo))
