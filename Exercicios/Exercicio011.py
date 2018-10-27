#Developed by Henrique Treza

#Le um numero real e mostra na tela sua porção inteira

import math

numero = float(input('Insira um valor: '))
print('O numero insirido foi {} e a sua porção inteira é {}'.format(numero, math.trunc(numero)))