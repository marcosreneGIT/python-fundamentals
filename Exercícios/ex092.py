from datetime import datetime

dados = dict()
dados['nome'] = str(input('Informe seu nome: '))
data_nacimento = int(input('Informe seu ano de nascimento: '))
dados['idade'] = datetime.now().year - data_nacimento
dados['ctps'] = int(input('Informe o número de sua carteira de trabalho ([0] PARA NÃO POSSUI): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Informe o ano de sua contratação: '))
    dados['salário'] = float(input('Informe seu salário: R$'))
    dados['aposentadoria'] = dados['idade'] + 35 - (datetime.now().year - dados['contratação'])
print('\nInformações: ')
for k, v in dados.items():
    print(f'- {k}: {v}')
