'''
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo o usuário.
O programa será interrompido quando o número solicitado
for negativo.
'''
while True:
    n = int(input('Digite um número para ver sua tabuada: '))

    if n < 0:
        break

    print('=' * 13)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')

    print('=' * 13)
