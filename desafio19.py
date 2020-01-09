import random
print('='*10,' DESAFIO 19 ','='*10)
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))