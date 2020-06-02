'''
A Confederação Nacional de Natação precisa de
um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com
a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date

ano = int(input('Ano de nascimento: '))

idade = date.today().year - ano

if idade <= 9:
    print('Idade: {}.\nCategoria: MIRIM'.format(idade))
elif idade <= 14:
    print('Idade: {}.\nCategoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('Idade: {}.\nCategoria: JUNIOR'.format(idade))
elif idade <= 25:
    print('Idade: {}.\nCategoria: SÊNIOR'.format(idade))
else:
    print('Idade: {}.\nCategoria: MASTER'.format(idade))