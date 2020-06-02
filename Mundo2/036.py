'''
Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. O programa
vai perguntar o valor da casa, o salário do
comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo
que ela não pode exceder 30% do salário ou
então o empréstimo será negado.
'''

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos vai financiar? '))

prestação = casa / (anos * 12)

if prestação >= (salario * 0.3):
    print('O empréstimo foi \033[1;31mNEGADO\033[m, pois a prestação ocuparia {:.2f}% do seu salário. Ficando com parcelas de R${:.2f}'.format((prestação / salario) * 100, prestação))
else:
    print('O empréstimo foi \033[1;32mAPROVADO\033[m, pois ele só ocupará {:.2f}% do seu salário. Ficando com parcelas de R${:.2f}'.format((prestação / salario) * 100, prestação))