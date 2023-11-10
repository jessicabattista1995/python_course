from random import choice
a = str(input("Qual os nome do aluno 1 : "))
b = str(input("Qual os nome do aluno 2 : "))
c = str(input("Qual os nome do aluno 3 : "))
d = str(input("Qual os nome do aluno 4 : "))
lista= [a,b,c,d]
s = choice(lista)
print('O aluno escolhido foi {}'.format(s))