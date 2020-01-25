from random import  randint
print('='*10,' DESAFIO 45 ','='*10)
print("""
    Escolha:
     
      01 - Pedra
      02 - Papel
      03 - Tesoura

""")

sorteado = randint(1,3)
escolha = int(input('Escolha o numero do  elemento: '))

if escolha == 1:

    if sorteado == 1:
        print('Deu empate!!! o escolido pelo computador foi: Pedra')
    elif sorteado == 2:
        print('Empate!!! o escolido pelo computador foi: Papel')
    elif sorteado == 3:
        print('Você ganhou!!! o computador escolheu Tesoura')

elif escolha == 2:

    if sorteado == 1:
        print('Deu empate!!! o escolido pelo computador foi: Pedra')
    elif sorteado == 2:
        print('Empate!!! o escolido pelo computador foi: Papel')
    elif sorteado == 3:
        print('Você perdeu!!! o computador escolheu Tesoura')

elif escolha == 3:

    if sorteado == 1:
        print('Deu perdeu!!! o escolido pelo computador foi: Pedra')
    elif sorteado == 2:
        print('Ganhou!!! o escolido pelo computador foi: Papel')
    elif sorteado == 3:
        print('Você empate!!! o computador escolheu Tesoura')
