'''
Aprimore o desafio 093 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
'''
jogador = dict()
gols = list()
lista = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, partidas):
        gols.append(int(input(f'\tQuantos gols na partida {c}? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    lista.append(jogador.copy())

    gols.clear()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]

        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if resp == 'N':
        break

print('-=' * 30)
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for c, v in enumerate(lista):
    # print(f'{c:>3} {v["nome"]:<12} {v["gols"]!s:<16s} {v["total"]}')
    print(f'{c:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 43)

while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if n == 999:
        break

    if n >= len(lista):
        print(f'ERRO! Não existe jogador com o código {n}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[n]["nome"]}:')

        for c, v in enumerate(lista[n]['gols']):
            print(f'  No jogo {c} fez {v} gols.')