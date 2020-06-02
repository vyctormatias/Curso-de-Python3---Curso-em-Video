'''
Desenvolva uma lógica que leia peso e a altura
de uma pessoa. Mostre seu status, de acordo com
a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC {:.1f}. Abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC {:.1f}. Peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('IMC {:.1f}. Sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('IMC {:.1f}. Obesidade.'.format(imc))
else:
    print('IMC {:.1f}. Obesidade mórbida.'.format(imc))
