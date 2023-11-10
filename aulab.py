n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua nota foi boa, parabéns!')
else:
    print('Sua nota está abaixo da média. REPROVADO!!')

# or print('Parabéns if m >= 6.0)