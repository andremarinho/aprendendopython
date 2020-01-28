from builtins import input

print('='*10,' DESAFIO 35 ','='*10)
print("""
 Este programa pede a informação de 3 retas e diz
 se é possivel a formação de um triangulo.
""")

r1 = float(input('Digite o segundo segmento de uma reta: '))
r2 = float(input('Digite o segundo segmento de uma reta: '))
r3 = float(input('Digite o terceiro segmento de uma reta: '))



if (r1 <(r2+r3)) and (r2<(r1+r3)) and (r3<(r2+r1)):
    print('As retas formam um triangulo')
else:
    print('As retas não formam um triangulo')



