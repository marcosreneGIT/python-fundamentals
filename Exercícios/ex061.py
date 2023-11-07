primeiro_termo_pa = int(input('Digite o primeiro termo: '))
razao_pa = int(input('Digite a razão: '))
contador = 1
termos = primeiro_termo_pa
while contador <= 10:
    print(termos, end=' ')
    termos += razao_pa
    contador += 1
