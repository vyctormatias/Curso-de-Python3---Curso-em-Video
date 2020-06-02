'''
Crie uma programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços.

Ex:
- APOS A SOPA
- CIVIC
- A SACADA DA CASA
'''
frase = str(input('Entre com uma frase: ')).strip().upper().replace(' ', '')

inverso = frase[::-1]

# for c in range(len(frase) -1, -1, -1):
#     inverso += frase[c]

if frase == inverso:
    print('A frase É um palíndromo')
else:
    print('A frase NÃO é um palíndromo')