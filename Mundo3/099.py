'''
Faça um programa que tenha uma função chamada maior(), que
receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual
deles é o maior.
'''
from time import sleep

def maior(* num):
    print('-=' * 30)
    print('Analisando os valores informados...')
    for c in num:
        print(c, end=' ')
        sleep(0.3)
    print(f'Foram analisados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {0 if len(num) == 0 else max(num)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()