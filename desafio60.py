print('='*10,' DESAFIO 60 ','='*10)
print('''
    Este programa mostra a fatorial de um numero.''')

n1 = int(input('Digite um numero: '))
c = n1 -1
resultado = n1

while c != 1 and c != 0:

    resultado = (resultado * c)
    c = c -1


print('O resultado da fatorial de {} é {}'.format(n1,resultado))