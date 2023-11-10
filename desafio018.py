from math import radians,sin,cos,tan
a = float(input('Digite um ângulo:  '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O seno do ângulo {:.2f} é {:.2f} e o cosseno é {:.2f} e a tangente é {:.2f}'.format(a,sen,cos,tan))