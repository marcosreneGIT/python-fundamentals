print('10 termos de uma PA\n')
p_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
dec_termo = p_termo + (10 - 1) * razao
for c in range(p_termo, dec_termo + razao, razao):
    print(c, end=' -> ')
print('Fim')