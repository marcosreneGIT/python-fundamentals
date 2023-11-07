primeiro_termo_pa = int(input('Digite o primeiro termo: '))
razao_pa = int(input('Digite a razão: '))
termos_pa = primeiro_termo_pa
contador = 0
continuar_pa = True
total_termos = 10
mais_termos = 0
while continuar_pa:
    total_termos += mais_termos
    while contador < total_termos:
        print(termos_pa, end=' ')
        termos_pa += razao_pa
        contador += 1
    mais_termos = int(input('\n\nQuantos mais termos deseja saber desta PA: '))
    if mais_termos == 0:
        continuar_pa = False
print(f'\nPrograma finalizado.\n\nTotal de termos: {total_termos}')
