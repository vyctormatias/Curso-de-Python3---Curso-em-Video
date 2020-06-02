'''
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realize
a contagem.

Seu programa tem que realizar três contagens através da
função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
'''
from time import sleep

def contador(init, end, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1

    print('-=' * 30)
    print(f'Contagem de {init} até {end} de {step} em {step}')

    if init < end:
        for c in range(init, end, step):
            print(c, end=' ', flush=True)
            sleep(0.3)
    else:
        for c in range(init, end, -step):
            print(c, end=' ', flush=True)
            sleep(0.3)
        
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)