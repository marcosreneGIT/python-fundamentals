cores = ('\033[m',  # 0 - sem cor
         '\033[1;30;41m',  # 1 - fundo vermelho
         '\033[1;30;42m',  # 2 - fundo verde
         '\033[1;30;45m'   # 3 - fundo roxo
         )


def help_func(func):
    from time import sleep
    print('-'*30)
    print(f'{cores[2]}Acessando o manual do comando {func}...{cores[0]}\n')
    sleep(3)
    print(f'{cores[3]}', end='')
    help(func)
    print(cores[0])


while True:
    print('-'*30)
    print(f'{cores[2]}- Sistema de ajuda PyHelp -{cores[0]}')
    funcao = str(input(f'\n{cores[3]}Função ou bliblioteca: {cores[0]}')).strip().lower()
    if funcao == 'fim':
        print(f'\n{cores[1]}Programa encerrado.{cores[0]}')
        break
    help_func(funcao)
