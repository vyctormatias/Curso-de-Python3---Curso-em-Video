def leiaDinheiro(msg):
    while True:
        valor = str(input('Digite o preço: R$')).replace(',', '.').strip()
        if valor.replace('.', '').isdigit():
            break
        else:
            print(f'\033[0;31mERRO! "{valor}" é um preço inválido!\033[m')
    
    return float(valor)