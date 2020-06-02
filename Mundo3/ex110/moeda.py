def aumentar(v=0, p=0, f=False):
    res = v + (v * p / 100)
    return moeda(res) if f else res
    

def diminuir(v=0, p=0, f=False):
    res = v - (v * p / 100)
    return moeda(res) if f else res


def dobro(v=0, f=False):
    res = v * 2
    return moeda(res) if f else res


def metade(v=0, f=False):
    res = v / 2
    return moeda(res) if f else res

def resumo(v, aumento, reducao):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(v)}')
    print(f'Dobro do preço:  \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(v, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(v, reducao, True)}')
    print('-' * 30)

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
