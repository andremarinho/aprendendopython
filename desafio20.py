from random import  shuffle
print('=' * 10, ' DESAFIO 20 ', '=' * 10)
aluno1 = input('\033[1;31;40m Digite o nome do primeiro aluno:\033[m ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
