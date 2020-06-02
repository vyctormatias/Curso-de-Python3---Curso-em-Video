'''
Faça um programa que leia três números e mostre
qual é o maior e qual é o menor.
'''
n1 = int(input('Entre com o primeiro número: '))
n2 = int(input('Entre com o terceiro número: '))
n3 = int(input('Entre com o segundo número: '))
num = [n1, n2, n3]

print('{} é o maior.'.format(max(num)))
print('{} é o menor.'.format(min(num)))

# maior = n1
# if n2 > n3 and n2 > n1:
#     maior = n2
# if n3 > n1 and n3 > n2:
#     maior = n3

# menor = n1
# if n3 > n2 and n1 > n2:
#     menor = n2
# if n1 > n3 and n2 > n3:
#     menor = n3

# print('{} é o maior.'.format(maior))
# print('{} é o menor.'.format(menor))
