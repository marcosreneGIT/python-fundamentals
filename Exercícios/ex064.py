numeros = soma = cont_num = 0
while numeros != 999:
    numeros = int(input('Digite um número[999 PARA]: '))
    if numeros != 999:
        soma += numeros
        cont_num += 1
print(f'\nA soma de todos os {cont_num} é igual a {soma}')