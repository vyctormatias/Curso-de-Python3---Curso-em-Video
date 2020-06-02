'''
Faça um programa que leia o comprimento
do cateto oposto e do catero adjacente
de um triângulo retângulo, calcule e 
mostre o comprimento da hipotenusa 
'''

'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format(math.hypot(co, ca)))