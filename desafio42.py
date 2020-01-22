print('='*10,' DESAFIO 42 ','='*10)
r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))

if ( r1 < (r2 + r3)) and (r2 < (r1 + r3)) and (r3 < (r1 + r2)):
    print('As retas podem formar  um triangulo.')

    if r1 == r2 == r3:
        print('Trata-se de um triangulo equilatero')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Pode-se formar um triangulo Equilatero')
    else
        print('As retas podem formar um triangulo Escaleno')

else:
    print('As retas \033[31;1m não \033[m formam um triangulo.')