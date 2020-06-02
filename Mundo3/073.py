'''
Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol', 'na ordem de
colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time do Corinthians.

# Pesquisar tabela do brasileirão no google
'''
times = ('Athletico Paranaense', 'Atlético', 'Atlético', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 
'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Vasco da Gama')

print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Corinthians está na {times.index("Corinthians") + 1}ª posição')
print('-=' * 15)
