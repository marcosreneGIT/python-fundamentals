from random import randint
from time import sleep
jogada_pc = randint(0, 2)
intens = ('PEDRA', 'PAPEL', 'TESOURA')

print('-' * 8, 'JO KEN PO', '-' * 8)
print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
jogada_p1 = int(input('Jogue: '))

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-'*45)
print('Você jogou {} e o computador jogou {}.'.format(intens[jogada_p1], intens[jogada_pc]))
if jogada_p1 == jogada_pc:
    print('EMPATE')
elif jogada_p1 == 0 and jogada_pc == 2 or jogada_p1 == 1 and jogada_pc == 0 or jogada_p1 == 2 and jogada_pc == 1:
    print('\033[32mVOCÊ VENCEU')
else:
    print('\033[31mVOCÊ PERDEU')
