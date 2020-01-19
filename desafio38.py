print('='*10,' DESAFIO 38 ', '='*10)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O primeiro numero {} é maior que o segundo {}'.format(n1,n2))
elif  n2 > n1:
    print('O segundo numero {} é maior que o primeiro {}'.format(n2,n1))
else:
    print('Os nuemros {}  e {} são iguais.'.format(n1,n2))