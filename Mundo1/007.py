'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
'''
n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))

print('A média ente {} e {} é: {:.1f}'.format(n1, n2, (n1+n2)/2))