'''
Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00, calcule um
aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.
'''
s = float(input('Qual o salário? R$'))

if s > 1250:
    print('Com o aumento de 10% o novo salário é de R${:.2f}.'.format(s * 1.1))
else:
    print('Com o aumento de 15% o novo salário é de R${:.2f}.'.format(s * 1.15))