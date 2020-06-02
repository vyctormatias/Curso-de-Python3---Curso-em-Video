'''
Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
'''
pessoa = dict()
agenda = list()
soma = 0

while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]

        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    agenda.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        
        if resp in 'SN':
            break

        print('ERRO! Responda apenas S ou N.')
    
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(agenda)} pessoas cadastradas.')

média = soma / len(agenda)

print(f'B) A média de idade é de {média:.2f} anos.')

print(f'C) As mulheres cadastradas foram', end=' ')
for c in agenda:
    if c['sexo'] in 'F':
        print(c['nome'], end='; ')
print()

print(f'D) Lista das pessoas que estão acima da média:')
for c in agenda:
    if int(c['idade']) >= média:
        print('   ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
