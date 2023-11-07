def leia_int(a: str):
    while True:
        try:
            n = int(input(a))
            return n
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor inteiro valido.\033[m\n')
        except KeyboardInterrupt:
            print('\n\n\033[31mPrograma interrompido.\033[m')
            break


def leia_float(a: str):
    while True:
        try:
            n = float(input(a))
            return n
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor real valido.\033[m\n')
        except KeyboardInterrupt:
            print('\n\n\033[31mPrograma interrompido.\033[m')
            break


num_0 = leia_int('Digite um  número inteiro: ')
num_1 = leia_float('Digite um número real: ')
print(f'\nVocê digitou o valor inteiro: {num_0}')
print(f'Você digitou o valor real: {num_1}')
