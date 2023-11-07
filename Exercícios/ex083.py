expressao = str(input('Digite a sua expressão númerica: '))
pilha = []
for simbolos in expressao:
    if simbolos == '(':
        pilha.append('(')
    elif simbolos == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print()
if len(pilha) == 0:
    print('Valida.')
else:
    print('Invalida.')

