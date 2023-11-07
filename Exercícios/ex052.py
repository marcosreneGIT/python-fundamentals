num = int(input('Digite um número: '))
print('')
cont_div = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m{}'.format(c), end=' ')
        cont_div += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
print('\n\nO número {} foi divisível {} vezes.'.format(num, cont_div))
if cont_div == 2:
    print('E por isso se trata de um número primo.')
else:
    print('Sendo assim impossível de ser um número primo.')
