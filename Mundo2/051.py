'''
Desenvolva um programa que leia o primeiro termo e a
razão de uma PA (progressão aritimética). No final,
mostre os 10 primeiros termos dessa progressão.
'''
n = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

for c in range(0, 10):
    print(n, end=' ')
    n += razão

print()
