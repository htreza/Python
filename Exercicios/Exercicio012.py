#Developed by Henrique Treza

#Leitura do cateto opost e do cateto adjacente de um triangulo retangulo

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** (1/2)) sem importação da classe math
hi = math.hypot(co, ca)
print('A hipotenusa tem a medida {:.2f}'.format(hi))

