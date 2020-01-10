print('='*10,' DESAFIO 24 ','='*10)
print("""Este programa pede para o usuario digitar o nome 
da cidade onde ele nasceu e retornar true ou false se o 
nome contém a palavra santo""")

cidade = str(input('Digite a cidade onde você nasceu: ')).strip()

print(cidade[0:5].upper() == 'SANTO')