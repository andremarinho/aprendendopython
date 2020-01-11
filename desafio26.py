print('='*10,' DESAFIO 26 ','='*10)
frase = str(input('Digite seu nome completo: ').strip().upper())
print('A letra A aparece {} vezes na frase. '.format(frase.count('A')))
print('A letra A aparece pela primeira vez a posição {}.'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}.'.format(frase.rfind('A')+1))

