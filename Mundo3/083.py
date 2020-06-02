'''
Crie um programa onde o usuário digite uma expressão
qualquer que use parênteses. Seu programa deverá
analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta. 
'''
exp = str(input('Digite a expressão: '))
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
