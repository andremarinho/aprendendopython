print('='*10, ' DESAFIO 48 ','='*10 )
soma = 0

for c in range(1,501,2):

   if (c % 3) == 0:
        soma += c

print('O valor total da soma dos multiplos de 3 entre 1 e 500 é de {}'.format(soma))