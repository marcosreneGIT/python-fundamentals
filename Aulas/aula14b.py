cont_par = 0
cont_impar = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 0:
        break
    if num % 2 == 0:
        cont_par += 1
    else:
         cont_impar += 1
print(f'\nTotal de pares: {cont_par}\nTotal de impares: {cont_impar}')