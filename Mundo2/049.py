'''
Refaça o desafio 009, mostrando a tabuada de um
número que o usuário escolher, só que agora
utilizando um laço for.
'''
n = int(input('Entre com o número que deseja ver a tabuada: '))

print('-=' * 7)
for c in range(1, 11):
    print('{} x {:2} = {}'. format(n, c, n*c))
    
print('-=' * 7)