'''
Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de
parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles.
'''
total = soma = n = 0

while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        total += 1
        soma += n

print('Foram digitados {} números, e a soma entre eles é {}'.format(total, soma))