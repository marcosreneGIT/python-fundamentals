def voto(ano):
    """
    - função criada com a intenção de informe a responsabilade de cada um com o voto
    baseando-se na idade da pessoa.

    :param ano: ano de nascimento.
    :return: se é autorizado, não autorizado ou opcional o voto.
    """
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Idade {idade} anos: \033[31mVoto não autorizado\033[m.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Idade {idade} anos: \033[33mVoto opcional\033[m.'
    else:
        return f'Idade {idade} anos: \033[32mVoto obrigatorio\033[m.'


ano_nasc = int(input('Informe o ano de seu nascimento: '))
print(voto(ano_nasc))
