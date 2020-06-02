'''
Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita
que o usuário possas mostrar as notas de cada aluno
individualmente.
'''
lista = []

while True:
    nome = str(input('Nome: '))

    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    media = ((n1 + n2) / 2)

    lista.append([nome, [n1, n2], media])

    resp = str(input('Quer continuar? [S/N]: '))

    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, v in enumerate(lista):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')

while True:
    print('-' * 35)
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if resp == 999:
        break
    elif resp <= len(lista) - 1:
        print(f'Notas de {lista[resp][0]} são {lista[resp][1]}')
