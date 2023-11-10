print('-=-'*20)
print('                   Empréstimo Bancário         ')
print('-=-'*20)
casa = float(input('Digite o Valor do Imóvel: R$'))
salario = float(input('Digite o valor do seu Salário: R$ '))
anos = int(input('Digite a quantidade de anos: '))
prestacao = casa / (anos * 12)
exceder = salario * 30/100
if prestacao >= exceder:
    print('\033[0;31mInfelizmente a prestação mensal excede 30% do seu salário.\033[m')
else:
    print('O valor da prestação mensal fica em R$ {:.0f}'.format(prestacao))