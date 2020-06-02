'''
Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-os (com idade) em um dicionário. Se
por acaso a CTPS for diferente de zero, o dicionário
receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se
aposentar.
'''
from datetime import datetime
clt = dict()

clt['nome'] = str(input('Nome: '))

anoNasc = int(input('Ano de nascimento: '))
clt['idade'] = datetime.now().year - anoNasc
clt['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if clt['ctps'] != 0:
    clt['contratação'] = int(input('Ano de contratação: '))
    clt['salário'] = float(input('Salário: R$'))
    clt['aposentadoria'] = clt['contratação'] - anoNasc + 35

for k, v in clt.items():
    print(f'- {k} tem o valor {v}')