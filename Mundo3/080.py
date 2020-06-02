'''
Crie um programa onde o usuário possa digitar cinco
valores numéricos e cadastre-os em uma lista, já na
posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''
lista = []

for c in range(0, 5):
    num = int(input('Digite um valor: '))

    if not lista or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        for c, v in enumerate(lista):
            if num <= v:
                lista.insert(c, num)
                print(f'Adicionado na posição {c} da lista...')
                break

print('-=' * 40)
print(f'Os valores digitados em ordem foram {lista}')