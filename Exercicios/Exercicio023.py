# Developed by Henrique Treza


#Numero par ou impar

numero = int(input('Insira um numero para saber se ele é par ou impar: '))
resultado = numero % 2

if resultado == 0:
    print('Esse número "{}" é PAR'.format(numero))
else:
    print('Esse número "{}" é IMPAR'.format(numero))
