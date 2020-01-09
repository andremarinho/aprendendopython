print('='*10,' DESAFIO 22 ', '='*10)
print('Este programa vai analizar seu nome')
print('='*34)
nome = input('Digite seu nome completo: ')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.strip())-nome.count(' ')))
separado = nome.split();
print('Seu primeiro nome é {} e contém {} letras.'.format(separado[0],len(separado[0])))