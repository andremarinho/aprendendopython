print('='*10,' DESAFIO 56 ','='*10)

total_idade = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
qtd_mulheres_menos_20_anos = 0


for c in range(1,5):
    nome = input('Digite o nome da pessoa numero {}: '.format(c))
    idade = int(input('Qual a idade: '))
    sexo = input('Qual o sexo? ')

    total_idade +=  idade

    if sexo.upper() == 'M':

        if idade_homem_mais_velho < idade:

            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome

    if sexo.upper() == 'F':

        if idade < 20:

            qtd_mulheres_menos_20_anos += 1


print('A media de idade do grupo é {}'.format(total_idade / 4))
print('O nome do homem mais velho é {}'.format(nome_homem_mais_velho))
print('A quantidade de mulheres que tem menos de 20 anos: {}'.format(qtd_mulheres_menos_20_anos))
