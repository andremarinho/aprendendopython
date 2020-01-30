print('=',' DESAFIO 50 ', '='*10)

soma = 0
numeroUsuario = 0
for c in range (1,7):

   numeroUsuario = int(input('Escolha um numero: '))

   if numeroUsuario % 2 == 0:

        soma += numeroUsuario

print('O valor total da soma dos numeros pares foi: {}'.format(soma))