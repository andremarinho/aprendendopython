print('='*10,' DESAFIO 55 ','='*10)

maior = 0

menor = 0


for c in range(0,5):
    peso = int(input('Qual é o seu peso? '))

    if menor == 0:
        menor = peso

    if peso > maior:

        maior  = peso

    if peso < menor:

        menor = peso

print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))