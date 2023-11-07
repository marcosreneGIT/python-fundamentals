aluno = dict()
aluno['nome'] = str(input('Nome do aluno(a): '))
aluno['media'] = float(input(f'Informe a média de {aluno["nome"]}: '))
if aluno['media'] <= 5:
    aluno['situação'] = 'Reprovado'
elif 5 < aluno['media'] <= 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

print(f'\nAluno: {aluno["nome"]}\nMédia: {aluno["media"]}\nSituação: {aluno["situação"]}')

