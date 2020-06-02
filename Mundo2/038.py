'''
Escreva um programa que leia dois número inteiros
e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 < n2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
