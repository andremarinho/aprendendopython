print('='*10,' DESAFIO 41 ','='*10)

idade = int(input('Qual é a sua idade: '))

if idade <= 9:
    print('Você faz parte da categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Você faz parte da categoria Infantil')
elif idade > 14 and idade <= 19:
    print('Você faz parte da categoria Junior')
elif idade  > 19 and idade <= 20:
    print('Você faz parte da categoria Senior')
elif idade > 20:
    print('Você faz parte da categoria Master')
