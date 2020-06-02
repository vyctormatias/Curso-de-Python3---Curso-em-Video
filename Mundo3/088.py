'''
Faça um programa que ajude um jogador da mega sena a
criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import sample
from time import sleep

# cont = 0

# print('-' * 30)
# print('{:^30}'.format('JOGA NA MEGASENA') )
# print('-' * 30)

# num = int(input('Quantos jogos você quer que eu sorteie? '))

# print(f'{"-=" * 3} SORTEANDO {num} JOGOS {"-=" * 3}')

# jogo = [[] for x in range(num)]

# for c in range(0, num):
#     while True:
#         n = randint(1, 60)

#         if n not in jogo[c]:
#             jogo[c].append(n)
#             cont += 1

#         if cont >= 6:
#             break
#     cont = 0
#     jogo[c].sort()

#     print(f'Jogo {c + 1}: {jogo[c]}')
#     sleep(1)

# print(f'{"-=" * 4} < BOA SORTE! > {"-=" * 4}')

jogos=list()
n=int(input('Quantos jogos?: '))
for c in range(n):
  a=sorted(sample(range(1, 61), 6))
  jogos.append(a[:])
  print(f'Jogo {c+1}: {a}')
  sleep(0.5)