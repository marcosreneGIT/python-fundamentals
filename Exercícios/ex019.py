from random import choice

aluno_1 = input('Nome do primerio aluno: ')
aluno_2 = input('Nome do segundo aluno: ')
aluno_3 = input('Nome do terceiro aluno: ')
aluno_4 = input('Nome do quarto aluno: ')

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

print('O aluno escolhido para apagar o quadro foi: {}'.format(choice(lista)))
