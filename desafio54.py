from datetime import date
print('='*10,' DESAFIO 54 ','='*10)

maiores = 0
menores = 0
ano_atual = date.today().year

for c  in range(1,8):
    ano_nascimento = int(input('Digite o ano de nascimento da pessoa numero {}: '.format(c)))

    if (ano_atual - ano_nascimento) >= 18:
        maiores += 1

    else:

       menores += 1

print('Ao todo {} pessoas são maiores e {} são menores'.format(maiores, menores))