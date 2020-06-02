def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return i


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c += 1
    print(linha())

    opc = leiaInt('\033[0;32mSua Opção: \033[m')
    return opc