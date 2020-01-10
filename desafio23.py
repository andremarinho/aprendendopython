print('='*10,' DESAFIO 23','='*10)
print("""Programa que leia um numero de 0 a 9999'
e mostre na cada um dos digitos separados \n""")

num = int(input('Informe um numero: '))
print('Analizando o numero {} '.format(num))



print('A unidade é {} '.format(num // 1 % 10))
print('A dezena é {} '.format(num // 10 % 10))
print('A centena é {} '.format(num // 100 % 10))
print('A milhar é {} '.format(num // 1000 % 10))