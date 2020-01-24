print('='*10,' DESAFIO 44 ','='*10)

preco_produto = float(input('Digite o valor do produto: '))
print('Condições de pagamentos: ')
print("""
    Escolha as condições de pagamento:
        
        Digite 1 para: À vista dinheiro/cheque desconto 10%
        Digite 2 para: À vista no cartão: 5%
        Digite 3 para: Em 2X no cartão é preço normal
        Digite 4 para: Em 3x ou mais no cartão com acrescimento de 20%""")

cond_pag = int(input('Digite a condição de pagamento: '))

if cond_pag == 1:

    print('A condição de pagamento selacionada foi À vista \n e o  valor final de seu produto é de R$ \033[31m{}\033[m '.format(preco_produto - (preco_produto * 0.1100)))

elif cond_pag == 2:

    print('A condição de pagamento selecionada foi à vista no cartão \n e o valor final de seu produto é de R$ \033[31m{}\033[m'.format(preco_produto - (preco_produto * 0.05)))

elif cond_pag == 3:

    print('A condição de pagamento selecionada foi em 2x no cartão \n e o valor final de produto ficou por R$ \033[31m{}\033[m  e cada parcela de R$ \033[31m{}\033[m'.format(preco_produto, preco_produto / 2))

elif cond_pag == 4:
    preco_final = preco_produto + (preco_produto * 0.2)
    parcela = preco_final / 3
    print('A condição de pagamento selecionada foi em 3x no cartão \n e o valor final de produto ficou em R$ \033[31m{}\033[m e cada parcela com valor de R$ \033[31m{}\033[m'.format(preco_final, parcela))