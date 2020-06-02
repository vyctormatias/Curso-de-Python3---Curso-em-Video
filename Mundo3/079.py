'''
Crie um programa onde o usuário possa digitar
vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele
não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem
crescente.
'''
lista = list()
while True:
    num = int(input('Digite um número: '))

    if num not in lista:
        lista.append(num)
        print('Número adicionado.')
    else:
        print('Número já existe. Não vou adicionar.')
    
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break

lista.sort()
print(f'Você digitou os valores {lista}')
