'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
'''
n = int(input('Entre com um número: '))

print('Dobro: {}\nTriplo: {}\nRaiz quadrada: {:.2f}'.format(n*2, n*3, pow(n,(1/2))))