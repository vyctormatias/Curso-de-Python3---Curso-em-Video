#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

escolha = choice(['PEDRA', 'PAPEL', 'TESOURA'])

jogada = str(input('Inicie sua jogada: ')).strip().upper()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ\n')

if escolha == 'PEDRA' and jogada == 'TESOURA' or escolha == 'PAPEL' and jogada == 'PEDRA' or escolha == 'TESOURA' and jogada == 'PAPEL':
    print('Vocẽ \033[31mPERDEU\033[m, escolhi {}!'.format(escolha.title()))
elif escolha == 'PEDRA' and jogada == 'PAPEL' or escolha == 'PAPEL' and jogada == 'TESOURA' or escolha == 'TESOURA' and jogada == 'PEDRA':
    print('Parabéns, você \033[32mVENCEU\033[m. Eu escolhi {}.'.format(escolha.title()))
else:
    print('Empate. Eu também escolhi {}.'.format(escolha.title()))
