from time import  sleep
print('='*10,' DESAFIO 51 ','='*10)
inicio = int(input('Digite o primeiro termo de uma P.A: '))
razao = int(input('Digite a razão de uma P.A: '))
sleep(1)
print('Os 10 primeiros termos da P.A são...')
final = (razao * 10 ) + inicio
for c in range(inicio, final, razao):
    print(c)