from time import sleep
print('='*10, ' DESAFIO 46 ', '='*10)
print('''
    Este programa faz uma contagem para estouro dos fogos de artificio, indo de 0 a 10.
''')

for c in range(1,11):
    print('Contagem regressiva para os fogos... {}'.format(c))
    sleep(1)

print('Brummmmm!!!!!!')