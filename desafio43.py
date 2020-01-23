print('='*10,' DESAFIO 43 ','='*10)
peso = float(input('Informe seu peso: '))
altura = float(input('Informa sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você esta abaixo do peso ideal. Seu IMC é de \033[31m{:.2f}\033[31m '.format(imc))

elif imc >= 18.5 and imc < 25:
    print('Você esta no peso ideal. Seu IMC é de \033[31m{:.2f}\033[m'.format(imc))

elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso. Seu IMC esta em \033[31m{:.2f}\033[m'.format(imc))

elif imc >= 30 and imc < 40:
    print('Você esta com obesidade. Seu IMC esta em \033[31m{:.2f}\033[m'.format(imc))

elif imc > 40:
    print('Você esta com obesidade morbida. Seu IMC esta em \033[31m{:.2f}\033[m'.format(imc))
