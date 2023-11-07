valor_saque = int(input('Informe o valor que deseja sacar: R$'))
cedula = 50
total_saque = valor_saque
contador_sedulas = 0
while True:
    if total_saque >= cedula:
        total_saque -= cedula
        contador_sedulas += 1
    else:
        if contador_sedulas > 0:
            print(f'Total de {contador_sedulas} cédula de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contador_sedulas = 0
        if total_saque == 0:
            break


