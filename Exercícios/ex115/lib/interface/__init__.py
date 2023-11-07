cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'neutro': '\033[m'}


def linha(tam_l=42):
    print('-' * tam_l)


def cabecalhos(txt, cor=cores['neutro'], tam_c=42):
    linha()
    print(f'{cor[0]}{txt.center(tam_c)}{cor[1]}')
    linha()


def menu(lista, cor=cores['neutro']):
    cabecalhos('MENU PRINCIPAL', [cores['verde'], cores['neutro']])
    opc_n = 1
    for opcao in lista:
        if opcao == 'SAIR DO SISTEMA':
            print(f'{cor[1]}{opc_n}{cor[0]} - {cor[3]}{opcao}{cor[0]}')
        else:
            print(f'{cor[1]}{opc_n}{cor[0]} - {cor[2]}{opcao}{cor[0]}')
        opc_n += 1
    linha()
    n = leia_int(f'{cores["verde"]}SUA OPÇÃO: {cor[0]}')
    return n


def leia_int(a: str):
    while True:
        try:
            n = int(input(a))
            return n
        except (ValueError, TypeError):
            cabecalhos('ERRO! DIGITE UM VALOR NUMERICO VALIDO.', [cores['vermelho'], cores['neutro']])
        except KeyboardInterrupt:
            cabecalhos('PROGRAMA INTERROMPIDO.', [cores['vermelho'], cores['neutro']])
            break
