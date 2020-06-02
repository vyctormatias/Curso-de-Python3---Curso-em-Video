'''
Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte ao usuário qual será o 
valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues.

Obs: Considere que o caixa possui cédulas de R$50m, R$20,
R$10 e R$1.
'''
valor = int(input('Qual o valor a ser sacado? R$'))

# cinquenta = valor // 50
# vinte = (valor % 50) // 20
# dez = ((valor % 50) % 20) // 10
# um = ((valor % 50) % 20) % 10

# print(f'Serão entregues:\n{cinquenta} notas de 50\n{vinte} notas de 20\n{dez} notas de 10\n{um} notas de 1')

total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
            
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1

        totcéd = 0

        if total == 0:
            break