print('='*10,' DESAFIO 31 ','='*10)
distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    print('O preço da passagem é R$ {}'.format(distancia * 0.50))
else:
    print('O preço da passagem é de R$ {}'.format(distancia * 0.45))