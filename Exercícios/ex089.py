boletim = []
nomes = []
notas = []
medias = []
while True:
    media = 0
    nome = str(input('Digite o nome: ')).split()
    nomes.append(nome)
    for i in range(0, 2):
        nota = float(input(f'Digite a {i + 1}° nota: '))
        notas.append(nota)
        media += notas[i]
    media = media / 2
    medias.append(media)
    notas.append(medias[:])
    nomes.append(notas[:])
    boletim.append(nomes[:])
    nomes.clear()
    medias.clear()
    notas.clear()
    while True:
        continuar = str(input('\nDeseja registrar mais um aluno? [S/N]: ')).upper().split()[0]
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('Opção invalida. Tente novamente.')
    if continuar == 'N':
        break
print('\nN°.  Nome     Média\n', '-' * 20)
for i, dados in enumerate(boletim):
    print(f'{i}   {dados[0][0]}     {dados[1][2][0]}')
while True:
    i_aluno = int(input('\nInforme o aluno que deseja saber as notas [[-1] CANCELAR]: '))
    print()
    if i_aluno == -1:
        break
    elif 0 <= i_aluno < len(boletim):
        print(f'Aluno: {boletim[i_aluno][0][0]}')
        for i in range(0, 2):
            print(f'{i + 1}° nota: {boletim[i_aluno][1][i]}')
    else:
        print('Número de aluno não registrado.')
print('Programa encerrado.')
