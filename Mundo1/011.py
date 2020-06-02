'''
Faça um programa que leia a largura e altura de uma parede em metros, calcule
a sua área e a quantidade de tintas necessárias para pintá-la, sabendo que cada
litro de tinta, pinta uma área de 2m²
''' 
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

print('Para pintar essa parede serão necessários {}lt de tinta'.format((altura*largura) / 2))