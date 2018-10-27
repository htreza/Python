#Developed by Henrique Treza

# Seno, Cosseno e tangente de um angulo
import math

angulo = float(input('Insira o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f} e o cosseno é de {:.2f} e tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))