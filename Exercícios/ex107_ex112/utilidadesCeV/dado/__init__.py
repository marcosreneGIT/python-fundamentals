def leia_dinheiro(n: str):
    while True:
        val = str(input(n)).replace(',', '.').strip()
        if val.isalpha() or val == '':
            print(f'\033[31mERRO! \"{val}\" é um preço invalido.\033[m')
        else:
            return float(val)


def leia_int(n: str):
    while True:
        val = input(n)
        if val.isnumeric():
            val = int(val)
            return val
        else:
            print('\n\033[31mERRO! Digite um valor númerico.\033[m\n')

