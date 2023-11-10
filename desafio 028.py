import random
n = int(input('Vou pensar entre um número 0 e 5 , tente advinhar? '))
print('==='*20)
print('Hummmm , deixa eu pensar....')
print('==='*20)
escolhido = random.randint(0,5)
if n == escolhido:
    print('Parabéns, você me ganhou!')
else:
    print('Puxa, você perdeu! \n O numero escolhido foi {:.0f} e não o {:.0f}. '.format(escolhido,n))
