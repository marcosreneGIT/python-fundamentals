from datetime import date

ano_atual = int(input('Informe um ano ([0] para saber o ano atual'))

if ano_atual == 0:
    ano_atual = date.today().year
if ano_atual % 4 == 0 and ano_atual % 100 != 0 or ano_atual % 400 == 0:
    print('{} é um ano bissexto'.format(ano_atual))
else:
    print('{} não é um ano bissexto'.format(ano_atual))



