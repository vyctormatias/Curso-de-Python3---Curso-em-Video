'''
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.

A multa vai custar R$7,00 por casa km acima do limite.
'''

vel = int(input('Qual a velocidade do carro? '))

if vel > 80:
    print('Você foi multado! O valor da multa é de: R${:.2f}'.format(7.0 * (vel - 80)))
else:
    print('Pode seguir tranquilamente!')