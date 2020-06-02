'''
Crie um programa que leia o nome de uma
cidade e diga se ela começa ou não com
o nome "SANTO".
'''
cidade = input('Entre com o nome da cidade: ')
nome = cidade.split()[0].upper()
print(nome == 'SANTO')
#print('SANTO' in nome)
#print(cidade[:5].upper() == 'SANTO')