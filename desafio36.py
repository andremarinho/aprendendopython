print('='*10,' DESAFIO 36 ','='*10)
valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Qual é o seu salario? '))
tempo_pag = int(input('Digite em quantos anos você quer pagar? '))
parcela = valor_casa / (tempo_pag * 12)

if parcela < (salario * 0.3):
    print('O valor da parcela ficou em R$ {:.2f} e o emprestimo foi aprovado para você pagar em {} meses'.format(parcela,tempo_pag*12))
else:
    print('O emprestimo foi negado, pois a parcela ficou em R$ {:.2f}, isso ultrapassa seu limite de pagamento'.format(parcela))