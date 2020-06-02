'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles.
'''
soma = total = 0

while True:
    n = int(input('Digite um número: '))

    if n == 999:
        break

    soma += n
    total += 1

print(f'Foram digitados {total} números, e a soma entre eles é {soma}.')
