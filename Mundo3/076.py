'''
Crie um programa que tenha uma tupla única com nomes de
produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os
dados em forma tabular.
'''
produtos = ('Arroz', 18.9,
        'Feijão', 8.6,
        'Iorgute', 4.3,
        'Bombril', 1.6,
        'Leite', 4.1)

print('-' * 40)
print('{:^40}'.format(' LISTAGEM DE PREÇOS '))
print('-' * 40)

for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<30}R${produtos[c + 1]:>7.2f}')
print('-' * 40)