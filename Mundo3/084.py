'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
pessoas = list()
lista = list()
peso = list()

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    lista.append(pessoas[:])
    peso.append(pessoas[1])
    pessoas.clear()

    resp = str(input('Quer continuar? [S/N]: '))

    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, {len(lista)} pessoas foram cadastradas.')
print(f'O maior peso foi de {max(peso):.1f}. Peso de', end=' ')
for c in lista:
    if c[1] == max(peso):
        print(f'[{c[0]}]', end=' ')
print()
print(f'O menor peso foi de {min(peso):.1f}. Peso de', end=' ')
for c in lista:
    if c[1] == min(peso):
        print(f'[{c[0]}]', end=' ')
print()
