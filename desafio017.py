import math
co=float(input('Cateto Oposto: '))
ca=float(input("Cateto Adjacente: "))
h=math.hypot(co,ca)
print('O comprimento da hipotenusa é {:.2f}'.format(h))