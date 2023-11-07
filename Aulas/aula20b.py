lista = [2, 5, 6, 9]


def somar(* numeros):
   soma = 0
   for numero in numeros:
      soma += numero
   print(soma)


def contador(* numeros):
   for valor in numeros:
      print(valor, end=' ')
   print(f'\nO total de números foram: {len(numeros)}')


def dobrar(valores):
   i = 0
   while i < len(valores):
      valores[i] *= 2
      print(valores[i], end=' ')
      i += 1


somar(5, 3)
somar(3, 5, 5)
print()
contador(2, 3, 5, 6)
dobrar(lista)
