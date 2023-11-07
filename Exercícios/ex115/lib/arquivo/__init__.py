from ex115.lib.interface import *


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    from time import sleep
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        cabecalhos('HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO!', [cores['vermelho'], cores['neutro']])
    else:
        cabecalhos('ARQUIVO SENDO CRIADO...', [cores['verde'], cores['neutro']])
        sleep(3)


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        cabecalhos('ERRO AO LER O ARQUIVO!', [cores['vermelho'], cores['neutro']])
    else:
        cabecalhos('PESSOAS CADASTRADAS', [cores['azul'], cores['neutro']])
        for linhas in a:
            dado = linhas.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{cores["azul"]}{dado[0]:<30}{cores["neutro"]}{cores["amarelo"]}{dado[1]:>3} anos{cores["neutro"]}')
    finally:
        a.close()


def cadastrar(arq, nm='DESCONHECIDO', idd=0):
    try:
        a = open(arq, 'at')
    except:
        cabecalhos('ERRO NA ABERTURA DO ARQUIVO', [cores['vermelho'], cores['neutro']])
    else:
        try:
            a.write(f'{nm};{idd}\n')
        except:
            cabecalhos('ERRO AO ESCREVER OS DADOS', [cores['vermelho'], cores['neutro']])
        else:
            cabecalhos('REGISTRO FEITO COM SUCESSO!', [cores['verde'], cores['neutro']])
        finally:
            a.close()

