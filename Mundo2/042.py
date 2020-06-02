'''
Refaça o desafio 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
r1 = float(input('Entre com o valor da primeira reta: ')) 
r2 = float(input('Entre com o valor da segunda reta: '))
r3 = float(input('Entre com o valor da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Essas retas podem formar um triângulo ', end='')
    #if r1 == r2 and r3 == r1:
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Essas retas NÂO podem formar um triângulo.')