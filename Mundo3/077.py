'''
Crie um programa que tenha uma tupla com várias palavras.
Depois disso, você deve mostrar, para cada palavra, quais
são as suas vogais.
'''
palavras = ('aprender', 'jogar', 'cozinhar', 'programar', 'python', 'linguagem', 'estudar', 'praticar')

# for c in range(0, len(palavras)):
for c in palavras:
    print(f'Na palavara {c.upper()} temos', end=' ')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()
