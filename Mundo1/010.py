'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
Considere US$ 1,00 = R$ 3,27
'''
r = float(input('Quanto dinheiro você tem na carteira? R$'))

print('Com esse dinheiro, você consegue comprar U${:.2f}'.format(r / 3.27))