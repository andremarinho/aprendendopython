from time import sleep
print('='*10,' DESAFIO 48 ','='*10 )

numero = int(input('Escolha um numero:'))
print('A tabuada do numero {} é...'.format(numero))
sleep(1)
for c in range  (1,10):
    print(' {} X {} = {}'.format(numero,c,numero * c))