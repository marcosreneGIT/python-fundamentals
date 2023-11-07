nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))
media = (nota_1 + nota_2) / 2

print('Sua media foi {:.1f}'.format(media))
print('APROVADO'if media >= 6 else'REPROVADO')
