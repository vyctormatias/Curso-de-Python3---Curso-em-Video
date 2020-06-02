'''
Refaça o desafio 051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
'''
n = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

cont = 0

while cont < 10:
    print(n, end=' ')
    n += razão
    cont += 1

print()