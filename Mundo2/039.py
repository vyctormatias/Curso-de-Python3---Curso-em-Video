'''
Faça um programa que leia o ano de um nascimento
de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que
falta ou que já passou do prazo.
'''
from datetime import date

nasc = int(input('Qual o seu ano de nascimento? '))
ano = date.today().year
idade = ano - nasc

if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print('Você ainda vai se alistar no serviço militar. Faltam {} ano(s).'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(ano + (18-idade)))
else:
    print('Já passou {} ano(s) do alistamento. Corra para se alistar!'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano + (18-idade)))
