'''
Crie um pacote chamado utilidadesCeV que tenha dois módulos
internos chamados moeda e dado.

Transfira todas as funções utilizadas nos desafios 107, 108,
109 e 110 para o primeiro pacote e manteira tudo funcionando.
'''
from utilidadesCeV import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)