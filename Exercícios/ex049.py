num = int(input('Informe o número que deseja saber a tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, (num * c)))
