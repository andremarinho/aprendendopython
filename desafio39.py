from datetime import  date


print('='*10,' DESAFIO 39 ','='*10)
ano_nascimento = int(input('Indforme seu ano de nascimento: '))
ano_atual = date.today().year

if (ano_atual - ano_nascimento) == 17:
    print('Já esta na hora de se alistar no exercito.')
elif (ano_atual - ano_nascimento) < 17:

    print('Você ainda precisa esperar {} anos para se alistar'.format(17 - (ano_atual - ano_nascimento)))

elif (ano_atual - ano_nascimento) > 17:
    print('Você tem que se apresentar ao exercito e pagar uma multa pelo atraso de {} anos'.format((ano_atual - ano_nascimento) - 17))