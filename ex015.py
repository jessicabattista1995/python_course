km=float(input('Quantos km percorridos? '))
dias=int(input('Quantos dias foi utilizado? '))
t=(km*0.15)+(dias*60)
print('O valor a ser cobrado é de R$ {:.2f}'.format(t))
