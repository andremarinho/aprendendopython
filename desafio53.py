from builtins import print

print('='*10,' DESAFIO 53 ','='*10)

frase = input('Digite uma frase pra saber ')

frase = frase.replace(" ","")
frase  = frase.upper();

frasepalindromo = True

for c in range(0,len(frase)):

    if(frase[c] != frase[((len(frase) - 1)-c)]):
        print('Opa, encontrei uma diferença! o caracter da frase é {} e o seu oposto é {}'.format(frase[c],frase[((len(frase) - 1)-c)]))
        frasepalindromo = False


if(frasepalindromo):
    print('A frase é um palindromo.')
else:
    print('A frase \033[32mnão\033[m é um palindromo.')


