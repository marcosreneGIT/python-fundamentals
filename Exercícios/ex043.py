peso_kg = float(input('Informe seu peso (KG): '))
altura = float(input('Informe sua altura (M): '))
imc = peso_kg / (pow(altura, 2))

print('\nSeu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
