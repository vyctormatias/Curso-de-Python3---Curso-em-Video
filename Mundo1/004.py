'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas a s informações possíveis sobre ele
'''
n = input('Digite algo? ')
print(type(n))
print('É um número? ', n.isnumeric())
print('É um letra? ', n.isalpha())
print('É um decimal? ', n.isdecimal()) 
print('É um digito? ', n.isdigit())
print('É uma letra minúscula? ', n.islower())
print('É uma letra maiúscula? ', n.isupper())
print('É alfanumérico? ', n.isalnum())
print('É capitalizada? ', n.istitle())
print('É só espaço? ', n.isspace())
