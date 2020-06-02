'''
Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
'''
from datetime import date

ano = date.today().year
maiores = 0
menores = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if (ano - nasc) >= 18:
        maiores += 1
    else:
        menores += 1

print('Existem {} pessoas de maior, e {} pessoa(s) menor(e)s de idade'.format(maiores, menores))
