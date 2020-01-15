print('='*10,' DESAFIO 33 ','='*10)
print("""
Este programa pede para o usuário digitar 3 numero e diz qual é o menor 
e qual é o maior. """)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro nuemro: '))

menor = n1;
maior = 0;

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 <n2:
    menor = n3
maior = n1
if n2 > n1 and  n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior =  n3

print('O maior numero é {} e o menor numero é {}'.format(maior,menor))


