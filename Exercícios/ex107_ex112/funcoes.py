def aumento(val=0, taxa=0, moeda=True):
    """
    função para definir um aumento em um valor base.

    :param val: valor base
    :param taxa: porcentagem do aumento
    :param moeda: formataçao da moeda com base na função moedas()
    :return: valor com a taxa aplicada
    """
    preco = val + (val * taxa/100)
    if moeda:
        return moedas(preco)
    else:
        return preco


def diminuir(val=0, taxa=0, moeda=True):
    """
    função para definir um descoto em um valor base.
    :param val: valor base
    :param taxa: porcentagem do desconto
    :param moeda: formatação da moeda com base na função moedas()
    :return: valor com o desconto aplicado
    """
    preco = val - (val * taxa/100)
    if moeda:
        return moedas(preco)
    else:
        return preco


def dobro(val=0, moeda=True):
    """
    fução para dobrar o valor base
    :param val: valor base
    :param moeda: formataão da moeda com base na função moedas()
    :return: dobro do valor base
    """
    preco = val * 2
    if moeda:
        return moedas(preco)
    else:
        return preco


def metade(val=0, moeda=True):
    """
    funçao para diminuir pela metado o valor base
    :param val: valor base
    :param moeda: formatação da moeda com base na função moedas()
    :return: metade do valor base
    """
    preco = val / 2
    if moeda:
        return moedas(preco)
    else:
        return preco


def moedas(val=0, moeda='R$'):
    """
    função para formatar um valor base
    :param val: valor base
    :param moeda: definição do tipo de moeda
    :return: valor base formatado
    """
    return f'{moeda}{val:.2f}'.replace('.', ',')


def resumo(val=0, aum=0, des=0):
    """
    resumo do resultado do programa principal
    :param val: valor base
    :param aum: aumento
    :param des: desconto
    :return: um resumo tabelar
    """
    print('\n- Resumo do valor -'
          f'\nPreço analisado: \t{moedas(val)}'
          f'\nDobro do preço: \t{dobro(val)}'
          f'\nMetade do preço: \t{metade(val)}'
          f'\n{aum}% de aumento: \t{aumento(val, aum)}'
          f'\n{des}% de desconto: \t{diminuir(val, des)}')
