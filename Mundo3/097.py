'''
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~~~
  Olá, Mundo!
~~~~~~~~~~~~~~~
'''
def msg(frase):
    t = len(frase) + 4
    print('~' * t)
    print(f'  {frase}  ')
    print('~' * t)


msg(str(input('Entre com uma frase: ')))