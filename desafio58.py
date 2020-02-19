from random import randint
from time import sleep

print('-=-'*30)
print("="*10, ' DESAFIO 58','='*10)
print('-=-'*30)

print("""
ESTE PROGRAMA VAI FAZER O COMPUTADOR 'PENSAR' EM UM NUMERO
INTEIRO E PEDIR PARA O USUARIO ADVINHAR
""")
numeroComputador = randint(0,10) # Faz o computador sortear um numero
print('PROCESSANDO estou pensando em numero de 0 a 10...')
sleep(2)
numeroUsuario = int(input('Aposte em um numero: '))
tentativas_usuario = 0;

while numeroComputador != numeroUsuario:
    print('Você errou, tente novamente')
    tentativas_usuario = tentativas_usuario + 1
    numeroUsuario = int(input('Digite novo numero: '))

print('Você ganhou!!! o numero sorteado foi {} e você precisou de {} tentaivas para ganhar o jogo.'.format(numeroComputador, tentativas_usuario))