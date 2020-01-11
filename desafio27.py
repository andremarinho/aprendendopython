print('='*10,' DESAFIO 27 ','='*10)
nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split();
print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu ultimo nome é {}'.format(separado[len(separado)-1]))