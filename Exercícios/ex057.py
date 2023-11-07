sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe corretamente seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('\nVocê pertence ao sexo masculino.')
else:
    print('\nVocê pertence ao sexo feminino.')