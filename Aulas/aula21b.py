def somar(a, b, c=0):
    """
    - soma até 3 valores apresentados e mostra em tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f'A soma dos valores é igual a {s}\n')


somar(2, 5, 6)
somar(4, 3)


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')


a = 5
teste(a)
print(f'\na = {a}')

