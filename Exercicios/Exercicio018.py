#Developed by Henrique Treza

#Exercicio que lê número de 0 a ... e mostra cada digito separado

numero = int(input('Insira um número: '))
h = str(numero)
print('Verificando seu número {}'.format(numero))
print('Unidade: {}'.format(h[3]))
print('Dezena: {}'.format(h[2]))
print('Centena: {}'.format(h[1]))
print('Milhar: {}'.format(h[0]))
