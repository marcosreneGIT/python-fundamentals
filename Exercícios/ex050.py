soma_par = 0
for c in range(1, 7):
    num = int(input('Digite o {}°  número: '.format(c)))
    if num % 2 == 0:
        soma_par += num
print('A soma entre os valores pares é igual a {}'.format(soma_par))
