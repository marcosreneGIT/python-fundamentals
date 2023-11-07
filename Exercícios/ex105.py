def notas(*nota, sit=True):
    boletim = dict()
    boletim['quantidade'] = len(nota)
    boletim['maior'] = max(nota)
    boletim['menor'] = min(nota)
    boletim['media'] = sum(nota) / len(nota)
    if sit:
        if boletim['media'] >= 7:
            boletim['situação'] = 'Boa'
        elif 5 <= boletim['media'] < 7:
            boletim['situação'] = 'Media'
        else:
            boletim['situação'] = 'Ruim'
    return boletim


print(notas(3, 2, 9, 1, 10))

