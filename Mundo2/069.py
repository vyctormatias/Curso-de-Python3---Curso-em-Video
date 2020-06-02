'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''
maiores = homens = mulherMenor = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]

    if idade >= 18:
        maiores += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulherMenor += 1

    resp = str(input('Deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        print('-' * 40)
        break

print(f'Há {maiores} pessoas com mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'Há {mulherMenor} mulheres com menos de 20 anos.')