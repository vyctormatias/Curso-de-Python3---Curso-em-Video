'''
Faça um programa que leia um número inteiro
e diga se ele é ou não número primo.
'''
num = int(input('Digite um número: '))
count = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;33m', end='')
        count += 1
    else:
        print('\033[1;31m', end='')
    print('{}'.format(c), end=' ')

print('\n\033[mO número {} foi divisível {} vezes.'.format(num, count))
if count == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')