'''
Crie um programa que tenha a função leiaInt(), que vai
funcionar de forma semelhante à função input() do python,
só que fazendo a validação para aceitar apenas um valor
numérico.

Ex:
n = leiaInt('Digite um n')
'''
def leiaInt(msg):
    valor = 0

    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')