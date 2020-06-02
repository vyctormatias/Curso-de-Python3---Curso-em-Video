'''
Escreva um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma Sequência de Fibonacci. 
'''
# print('-' * 30)
# print('Sequência de Fibonacci')
# print('-' * 30)

# n = int(input('Entre com um número inteiro: '))

# t1 = 0
# t2 = 1

# print('{} → {}'.format(t1, t2), end='')
# cont = 3

# while cont <= n:
#     t3 = t1 + t2
#     print(' → {}'.format(t3), end='')
#     t1 = t2
#     t2 = t3
#     cont += 1

# print()

Nant = 1
Fibonacci = 0

n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))

while n > 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')