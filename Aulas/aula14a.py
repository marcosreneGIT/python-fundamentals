resp = 'Sim'
while resp == 'Sim':
    num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar [Sim/Não]: ')).strip().capitalize()
    print('')
print('Fim')