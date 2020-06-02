'''
Crie um programa que leia dois valores e mostre
um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada
em cada caso.
'''
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opt = 0

while opt != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opt = int(input('Sua opção: '))

    if opt == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif opt == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opt == 3:
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, max(n1, n2)))
    elif opt == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-' * 20)
    sleep(1.5)
