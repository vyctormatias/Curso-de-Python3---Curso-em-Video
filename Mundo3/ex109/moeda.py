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


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
