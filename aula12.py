nome = str(input('Qual o seu nome: '))

if nome.upper() == 'ANDRÉ':
    print('Quen nome lindo!')
elif nome.upper()=='PEDRO':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia, {}!'.format(nome))