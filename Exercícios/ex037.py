numero = int(input('Digite um número: '))
print('\n[1] Binário\n[2] Octal\n[3] Hexadecimal')
base_conv = int(input('\nEscolha sua base de conversão: '))

if base_conv == 1:
    print('O número {} convertido em binário é igual a {}'.format(numero, bin(numero)[2:]))
elif base_conv == 2:
    print('O número {} convertido em octal é igual a {}'.format(numero, oct(numero)[2:]))
elif base_conv == 3:
    print('O número {} convertido em hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('\033[31mOPÇÃO INVALIDA')
print('Fim do programa')