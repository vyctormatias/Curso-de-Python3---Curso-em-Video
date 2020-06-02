'''
Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.
'''
nome = input('Entre com o nome: ').split()

print('Primeiro: {}'.format(nome[0]))
#print('Último: {}'.format(nome[len(nome) - 1]))
print('Último: {}'.format(nome[-1]))
