from random import randint
from time import  sleep

itens = ('Pedra', 'Papel', 'Tesoura')
print(''' Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Escolha um item: '))
computador = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))

if computador == 0: #Computador Jogou Pedra

    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:

        print('JOGADA INVALIDA!!!')


elif computador == 1: #Computador jogou Papel

    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:

        print('JOGADA INVALIDA!!!')


elif computador == 2: #Computador jogou Tesoura

    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:

        print('JOGADA INVALIDA!!!')