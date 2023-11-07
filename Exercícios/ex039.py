from datetime import date


def alistamento():
    nasc = int(input('\nInforme o ano em que nasceu: '))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    print('\nVocê nasceu em {} e em {} você já completou ou irá completar os {} anos.'.format(nasc, ano_atual, idade))

    if idade < 18:
        print('Faltam {} anos para o seu alistamento.'.format(18 - idade))
        print('A data prevista está para o ano de {}.'.format(ano_atual + (18 - idade)))
    elif idade > 18:
        print('Seu alistamento deveria ter sido a {} anos atras.'.format(idade - 18))
        print('A data era prevista para o ano de {}.'.format(ano_atual - (idade - 18)))
    else:
        print('Seu alistamento deve ser feito IMEDIATAMENTE.')
        print('Procure o orgão responsavel mais próximo.')


print('ALISTAMENTO MILITAR\n')
print('[1] Masculino\n[2] Feminino')
sexo = int(input('Informe seu sexo: '))

if sexo == 2:
    print('\nÉ preciso lhe informar que o alistamento em caso do sexo feminino não se torna algo obrigatorio.\n')
    print('[1] Confirmar\n[2] Cancelar')
    conf = int(input('Deseja continuar: '))
    if conf == 1:
        alistamento()
    elif conf == 2:
        print('Pedido de alistamento cancelado com sucesso.')
    else:
        print('\033[31mOPÇÃO INVALIDA')

if sexo == 1:
    alistamento()

print('\nFim do programa.')


