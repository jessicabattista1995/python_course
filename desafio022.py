nome = str(input('Nome Completo: ')).strip()
print('Analisando seu nome...')
maiusculas = nome.upper()
minusculas = nome.lower()
letras = len(nome) - nome.count(' ')
letras02 = nome.find(' ')
print('''Seu nome em maúsculas é {}
seu nome em maiúscula é {}  e
seu nome tem ao todo {} letras 
 Seu primeiro nome tem {} letras '''.format(maiusculas,minusculas,letras,letras02))
## ou para contar o primeiro nome também
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0],len(separa[0]))