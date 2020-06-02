'''
Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, crie duas listas extras que
vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um número: ')))

    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break

for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print('-=' * 40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')