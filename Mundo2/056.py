'''
Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos. 
'''
media = 0
contador = 0
maiorIdade = 0

for c in range(1, 5):
    nome = str(input('Nome da {}º pessoa: '.format(c)))
    idade = int(input('Idade da {}º pessoa: '.format(c)))
    sexo = str(input('Sexo da {}º pessoa [M/F]: '.format(c)))

    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        homemVelho = nome

    if sexo in 'Ff' and idade < 20:
        contador += 1

    media += idade
    print()

print('A média de idades do grupo é {} anos'.format(media / 4))
print('{} é o homem mais velho.'.format(homemVelho))
print('Há {} mulher(es) menor(es) de 20 anos no grupo'.format(contador))