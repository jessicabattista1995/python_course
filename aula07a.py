n1=int(input('um valor: '))
n2=int(input('Outro valor: '))
s=n1 + n2
m = n1 * n2
d = n1/n2
di= n1//n2
e = n1**n2
print('A soma vale {}\n o produto é {} \n e a divisão {:.3f}'.format(s,m,d), end=' ')
print('\nA divisão inteira é {}\n e a potência é {}\n'.format(di,e))