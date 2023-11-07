nota_1 = float(input('Informe sua primeira nota: '))
nota_2 = float(input('Informe sua segunda nota: '))
media = (nota_1 + nota_2) / 2

print('Com as notas no valor de {:.1f} e {:.1f} sua media ficou em {:.1f}\n'.format(nota_1, nota_2, media))

if media < 5:
    print('Você foi reprovado.')
elif 5 <= media < 7:
    print('Você está de recuperção.')
else:
    print('Você foi aprovado.')

