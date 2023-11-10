d = float(input('Digite a distância em KM: '))
ate = (d * 0.50)
acima = (d * 0.45)
if d <= 200:
    print('O valor da passagem a ser cobrado será de R${}'.format(ate))
else:
    print('O valor da passagem a ser cobrado será de R${}'.format(acima))

