num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite um número: '))

soma = num_1 + num_2
sub = num_1 - num_2
mult = num_1 * num_2
divi = num_1 / num_2
espo = num_1 ** num_2
divi_int = num_1 // num_2
modulo = num_1 % num_2

print('\nSendo posto os valores de {} e {}.\n\nSua soma: {}\nSua subtração: {}'.format(num_1, num_2, soma, sub), end='')
print('\nSeu produto: {}\nSeu quociente: {:.3f}\nSua potência: {}'.format(mult, divi, espo), end='')
print('\nSeu quociente inteiro: {}\nSeu modulo: {}'.format(divi_int, modulo))


