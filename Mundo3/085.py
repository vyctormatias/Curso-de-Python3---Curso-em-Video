'''
Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os
valores pares e ímpares em ordem crescente.
'''
lista = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram {sorted(lista[1])}')