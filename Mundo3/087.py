'''
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[], [], []]
pares = terColuna = segLinha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

        if c == 2:
            terColuna += matriz[l][c]

    print()
print('-=' * 30)
        
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terColuna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')