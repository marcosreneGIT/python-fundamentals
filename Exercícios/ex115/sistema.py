from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'
if arquivo_existe(arquivo):
    cabecalhos('ARQUIVO ENCONTRADO COM SUCESSO!', [cores['verde'], cores['neutro']])
else:
    cabecalhos('ARQUIVO NÃO ENCONTRADO!', [cores['vermelho'], cores['neutro']])
    criar_arquivo(arquivo)


while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVAS PESSSOAS', 'SAIR DO SISTEMA'],
                    [cores['neutro'], cores['amarelo'], cores['azul'], cores['vermelho']])
    match resposta:
        case 1:
            ler_arquivo(arquivo)
        case 2:
            cabecalhos('NOVO CADASTRO', [cores['azul'], cores['neutro']])
            nome = str(input(f'{cores["amarelo"]}INFORME O NOME: {cores["neutro"]}')).strip().upper()
            idade = leia_int(f'{cores["amarelo"]}INFORME A IDADE: {cores["neutro"]}')
            cadastrar(arquivo, nome, idade)
        case 3:
            cabecalhos("FINALIZANDO SISTEMA...", [cores['vermelho'], cores['neutro']])
            sleep(2)
            break
        case _:
            cabecalhos('ERRO! OPÇÃO INVALIDA. TENTE NOVAMENTE.', [cores['vermelho'], cores['neutro']])
    sleep(2)

