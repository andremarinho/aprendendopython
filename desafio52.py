print('='*10,' DESAFIO 52 ','='*10)
print('''
    Programa informa se o numero é primo ou não.
''')

numero = int(input('Informe um numero: '))
primo = True

for c in range(1, numero):

    if (c != 1)  and (numero % c == 0):
        primo = False
        print('Numero é divisivel por {}'.format(c))

if primo:
    print('O numero {} é primo.'.format(numero))
else:
    print('O numero {} não é primo.'.format(numero))