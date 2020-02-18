from random import randint
from time import sleep

print('-=-'*30)
print("="*10, ' DESAFIO 58','='*10)
print('-=-'*30)

print("""
ESTE PROGRAMA VAI FAZER O COMPUTADOR 'PENSAR' EM UM NUMERO
INTEIRO E PEDIR PARA O USUARIO ADVINHAR
""")
numeroComputador = randint(0,5) # Faz o computador sortear um numero
print('PROCESSANDO estou pensando em numero...')
sleep(2)
numeroUsuario = int(input('Aposte em um numero: '))

while numeroComputador != numeroUsuario:
    print('Você errou, tente novamente')
    numeroUsuario = int(input('Digite novo numero: '))

print('Você ganhou!!!' if numeroComputador == numeroUsuario else 'Você perdeu',' numero sorteador foi {}'.format(numeroComputador))