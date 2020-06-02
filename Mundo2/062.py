'''
Melhore o desafio 061, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.
'''
n = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

cont = 0
termos = 10

while cont < termos:
    print(n, end=' ')
    n += razão
    cont += 1

    if cont == termos:
        termos += int(input('\nDeseja mostrar mais quantos termos? '))

print('Progressão finalizada com {} termos mostrados.'.format(cont))