'''
Desenvolva um programa que pergunte a distância de
uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por
km para viagens de até 200km e R$0,45 para viagens
mais longas.
'''
dist = float(input('Qual a distância da viagem? '))

# print('O preço da passagem para essa viagem é de R$', end='')
# if dist <= 200:
#     print('{:.2f}.'.format(dist * 0.5))
# else:
#     print('{:.2f}.'.format(dist * 0.45))

preco = dist * 0.5 if dist <= 200 else dist * 0.45

print('O preço da passagem para essa viagem é de R${:.2f}'.format(preco))