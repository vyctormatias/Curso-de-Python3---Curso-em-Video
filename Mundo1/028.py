'''
Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu.
'''
#from random import randrange
from random import randint
from time import sleep

#n = randrange(6)
n = randint(0,5)

num = int(input('Adivinhe em qual número eu pensei? '))
print('Processando...')
sleep(2)

if num == n:
    print('Acertou!')
else:
    print('Errou! Eu pensei no número {}.'.format(n))
