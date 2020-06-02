'''
Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.
'''
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            print(c, 'x ' if c > 1 else '= ', end='')

    return fat


print(fatorial(5, True))