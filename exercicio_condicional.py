'''
tempo = int(input('Digite quantos anos tem seu carro?'))
if tempo<=3:
    print('Seu carro esta novinho')
else:
    print('Já esta na hora de trocar de carro')

print('Carro novo'if tempo<=3 else 'Carro velho')


nome = str(input('Digite seu nome: '))

if nome.upper() == 'ANDRÉ':
    print('Que nome lindo você tem!')
    print('Olá {}'.format(nome.upper()))
else:
    print('Ola {}'.format(nome.upper()))
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota'))
media = (n1+n2)/2

'''
if media >= 7:
    print('Você foi Aprovado')
else:
    print('Você foi reprovado')
'''

print('Você foi aprovado ' if media >= 7 else 'Foi foi reprovado')