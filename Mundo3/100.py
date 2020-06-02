'''
Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a
segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

def sorteia(num):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num.append(randint(1, 10))
        print(f'{num[c]}', end=' ')
        sleep(0.3)
    print('PRONTO!')

    return(numeros)


def somaPar(num):
    soma = 0

    for v in num:
        if v % 2 == 0:
            soma += v
    
    print(f'Somandos os valores pares de {num}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)