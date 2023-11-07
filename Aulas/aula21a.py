help(input)
print(print.__doc__)


def contador(ini, fin, pas):
    """
    - faz uma contagem e mostra em tela.

    :param ini: inicio da contagem
    :param fin: final da contagem
    :param pas: passo da contagem
    :return: sem retorno
    """
    for num in range(ini, fin + 1, pas):
        print(num, end=' ')


help(contador)
contador(0, 100, 10)
