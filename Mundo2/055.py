'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
for x in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(x)))

    if x == 1:
        maior = peso
        menor = peso

    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

print('O maior peso é {}Kg e o menor {}Kg'.format(maior, menor))