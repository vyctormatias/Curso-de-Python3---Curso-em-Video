def aumentar(v=0, p=0):
    return v + (v * p / 100)
    

def diminuir(v=0, p=0):
    return v - (v * p / 100)

def dobro(v=0):
    return v * 2


def metade(v=0):
    return v / 2


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
