'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
numeros = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(4))

print(f'Você digitou os valores {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O valor 3 foi digitado na {numeros.index(3) + 1}º posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')

print('Os números pares foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')

print()