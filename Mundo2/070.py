'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
'''
total = soma = cont = 0

while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço R$'))

    total += preço
    
    if preço > 1000:
        soma += 1

    if cont == 0 or preço < menor:
        menor = preço
        prodBarato = nome

    cont += 1

    opc = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if opc == 'N':
        break

    print('=' * 30)
print(f'O total de gasto na compra é de R${total}')
print(f'{soma} produtos custam mais de R$1000')
print(f'{prodBarato} é o produto mais barato')