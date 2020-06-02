'''
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
ranking = {}

for c in range(1, 5):
    jogo['jogador' + str(c)] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)