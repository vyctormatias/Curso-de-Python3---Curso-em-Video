'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
'''
from random import randint

cont = 0

print('=-' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 13)

while True:
    computador = randint(0,10)

    num = int(input('Sua jogada: '))

    soma = num + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]

    print('-' * 45)
    print(f'Você jogou {num} e eu joguei {computador}. Total deu {soma} que é {"PAR" if soma % 2 == 0 else "ÍMPAR"}')

    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    else:
        if soma % 2 == 1:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break

    print('Vamos jogar novamente...')

    print('-' * 45)

print(f'GAME OVER! Você venceu {cont} vezes.') 
