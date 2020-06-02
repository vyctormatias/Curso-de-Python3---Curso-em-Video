'''
Reescreva a função leiaInt() que fizemos n desafio 104,
incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função
leiaFloat() com a mesma funcionalidade.
'''
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


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except ValueError:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            f = 0
            break
        else:
            break
    return f


i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')