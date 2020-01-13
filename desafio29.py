from time import sleep

print('='*10,' DESAFIO 29 ','='*10)
velocidade = float(input('Em que velocidade esta o carro? '))

if velocidade <= 80:
    print('Boa viagem')

else:
    print('Você esta em alta velocidade e foi multado.')
    multa = 7 * (velocidade - 80)
    sleep(1)
    print('A sua multa foi de R$ {:2f} reais'.format(multa))