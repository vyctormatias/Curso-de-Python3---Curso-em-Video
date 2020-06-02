'''
Melhore o jogo do desafio 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando no
final quantos palpites foram necessários para vencer.
'''
from random import randint

n = randint(0, 10)

resp = ''
cont = 0

while resp != n:
    resp = int(input('Em qual número eu pensei? '))
    if n > resp:
        print('Maior...')
    elif n < resp:
        print('Menor...')
    cont += 1

print('Acertou!!! Foram você fez {} palpites até acertar.'.format(cont))