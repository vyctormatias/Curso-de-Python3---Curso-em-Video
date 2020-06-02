'''
Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores
lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores.
'''
p = ''
total = menor = maior = cont = 0

while p in 'Ss':
    n = int(input('Entre com um número inteiro: '))
    p = str(input('Deseja continuar a digitando valores? [S/N]: ')).strip()

    if cont == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    
    total += n
    cont += 1


print('A média dos valores digitados é: {:.2f}'.format(total / cont))
print('O maior valor lido foi o {} e o menor {}'.format(maior, menor))