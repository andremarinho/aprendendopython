print('='*10,' DESAFIO 59 ','='*10)
n1 = int(input('Digite o primeiro nuemro inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))
opcao = 0

while opcao != 5:
    print('''
        Digite [1] para Somar
        Digite [2] para multiplicar
        Digite [3] para maior numero
        Digite [4] novos numeros
        Digite [5] para finalizar o programa
    
    ''')
    print('='*30)
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('O resultado da soma é {}'.format(soma))
        input('Digite qualquer teclar para continuar...')

    if opcao == 2:
        soma = n1 * n2
        print('O resultado da multiplicaoção é {}'.format(soma))
        input('Digite qualquer teclar para continuar...')

    if opcao == 3:

        if n1 > n2:

            print('O numero {} é o maior.'.format(n1))

        elif n2 > n1:

            print('O numero {} é o maior.'.format(n2))

        else:

            print('Os numeros tem o mesmo valor {} .'.format(n1))

        input('Digite qualquer teclar para continuar...')

    if opcao == 4:

        n1 = int(input('Digite um novo numero para o primeiro numero : '))
        n2 = int(input('Digite um novo numero para o segundo numero: '))

    if opcao == 5:

        input('Saindo do programa, digite qualquer tecla para continuar...')
        opcao = 5