'''
Faça um programa que leia um número de0 a 9999
 e mostre na tela cada um dos digitos separados

 Ex:
 Digite um número 1834

 unidade:4
 dezena:3
 centena:8
 milhar:1
'''
n = int(input('Digite um número: '))

print('Unidade: {}'.format(n // 1 % 10))
print('Dezena: {}'.format(n // 10 % 10))
print('Centena: {}'.format(n // 100 % 10))
print('Milhar: {}'.format(n // 1000 % 10))