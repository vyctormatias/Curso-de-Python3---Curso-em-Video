'''
Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não
formar um triângulo.
'''
r1 = float(input('Entre com o valor da primera reta: '))
r2 = float(input('Entre com o valor da segunda reta: '))
r3 = float(input('Entre com o valor da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas NÂO podem formar um triângulo.')