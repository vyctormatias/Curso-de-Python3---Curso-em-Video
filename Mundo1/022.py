'''
Crie um programa que leia o nome completo
de uma pessoa e mostre:

* O nome com todas as letras maiúsculas
* O nome com todas minúsculas
* Quantas letras ao todo (sem considerar espaços)
* Quantas letras tem o primeiro nome
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
#print('O nome tem {} letras'.format(len(nome.replace(' ', ''))))
print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome tem {} letras'.format(len(nome.split()[0])))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))