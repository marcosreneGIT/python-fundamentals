def leia_int(n: str):
    while True:
        val = input(n)
        if val.isnumeric():
            val = int(val)
            return val
        else:
            print('\n\033[31mERRO! Digite um valor númerico.\033[m\n')


numero = leia_int('Digite um número: ')
print(f'\nVocê digitou o número {numero}.')