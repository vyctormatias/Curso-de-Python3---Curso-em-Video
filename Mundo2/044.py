'''
Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal
e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' LOJAS MATIAS '))
preço = float(input('Preço das compras: R$'))

print('Qual o tipo do pagamento: ')
opt = int(input('1) À vista dinheiro/cheque\n2) À vista no cartão\n3) Em até 2x no cartão\n4) 3x ou mais no cartão\n> '))

if opt == 1:
    total = preço * 0.9
elif opt == 2:
    total = preço * 0.95
elif opt == 3:
    total = preço
else:
    total = preço * 1.2

print('O preço à ser pago é R${:.2f}'.format(total))
