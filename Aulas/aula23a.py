try:
    numerador = int(input('Numerador: '))
    denominador = int(input('Denominador: '))
    resultado = numerador / denominador
except (ValueError, TypeError):
    print('\nERRO: Tivemos problemas com o tipo de dados que você digitou.')
except ZeroDivisionError:
    print('\nERRO: Não é possivel se dividir um númerador por zero.')
except KeyboardInterrupt:
    print('\n\nO usuário  preferiu não informar os dados.')
except Exception as erro:
    print(f'ERRO: {erro.__class__}')
else:
    print(f'\nO resultado é igual a {resultado:.2f}')
finally:
    print('Finalizando...')
