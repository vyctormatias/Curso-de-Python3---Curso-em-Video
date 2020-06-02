'''
Crie um pequeno sistema modularizado que permita cadastrar
pessoas pelo seu nome e idade em um arquio de texto simples.

O sistema só vai ter 2 opções: cadastrar uma nova pessoa
e listar todas as pessoas cadastradas.
'''
filename = "pessoas.txt"

while True:
    print('-' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('-' * 40)
    print('\033[0;33m1 -\033[0;34m Ver pessoas cadastradas\033[m')
    print('\033[0;33m2 -\033[0;34m Cadastrar nova pessoa\033[m')
    print('\033[0;33m3 -\033[0;34m Sair do sistema\033[m')
    print('-' * 40)

    opc = int(input('\033[0;32mSua opção: \033[m'))

    if opc == 1:
        print('-' * 40)
        print('PESSOAS CADASTRADAS'.center(40))
        print('-' * 40)

        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            print('Nenhuma pessoa foi cadastrada!')
        else:
            print(f.read())
    elif opc == 2:
        print('-' * 40)
        print('NOVO CADASTRO'.center(40))
        print('-' * 40)

        nome = str(input('Nome: '))
        idade = int(input('Idade: '))

        f = open(filename, 'a')
        f.write(f'{nome:<30}{idade} anos')
        f.close()

        print(f'Novo resgistro de {nome} adicionado.')
    elif opc == 3:
        print('-' * 40)
        print('SAINDO DO SISTEMA... ATÉ LOGO!'.center(40))
        print('-' * 40)
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')

