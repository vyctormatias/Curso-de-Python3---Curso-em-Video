'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, do zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))

    if 0 <= n <= 20:
        break
    print('Tente novamente.', end=' ')

print(f'Você digitou o número {numeros[n]}')