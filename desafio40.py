print('='*10,' DESAFIO 40 ','='*10)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    print('Você teve média \033[33m{}\033[m  e portanto estar reprovado.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {}  e esta em recuperação'.format(media))
else:
    print('Sua média foi \033[34m{}\033[m, parabéns!!! Você esta aprovado!'.format(media))