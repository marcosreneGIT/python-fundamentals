vel_carro = float(input('Informe sua velocidade: '))
multa = (vel_carro - 80) * 7

if vel_carro > 80:
    print('MULTADO!\nSerá cobrado um valor de R${:.2f} referente a multa.'.format(multa))
print('Tenha um bom dia! Dirija sempre com cuidado.')