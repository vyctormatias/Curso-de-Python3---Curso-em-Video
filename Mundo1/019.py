'''
Um professor quer sortear um dos seus
quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo
o nome deles e escrevendo o nome do
escolhido.
'''
from random import choice

aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

print('O aluno sorteado é {}'.format(
    choice([aluno1, aluno2, aluno3, aluno4])))