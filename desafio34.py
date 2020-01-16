from builtins import input

print('='*10,' DESSAFIO 34 ','='*10)
print("""
Este algoritmo calcula o aumento do salario de acordo 
com uma faixa salarial.""")

salario = float(input('Digite seu salario:  '))

if salario >= 1250:
    print('Seu salario atual é R$  {} e seu novo salario será R$ {}'.format(salario,salario+(salario*0.10)))
else:
    print('Seu salario atual é  R$ {} e seu novo salario será R$ {}'.format(salario, salario + (salario * 0.15)))