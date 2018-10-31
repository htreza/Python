#Developed by Henrique Treza

#Sorteio de uma pessoa aleatoria para ganhar um premio.
import random

nome1 = str(input('Insira o primeiro nome: '))
nome2 = str(input('Insira o segundo nome: '))
nome3 = str(input('Insira o terceiro nome: '))
nome4 = str(input('Insira o quarto nome: '))
nome5 = str(input('Insira o quinto nome: '))
lista = [nome1, nome2, nome3, nome4, nome5]

escolha = random.choice(lista)

print('Parabens!!!! {}, voce acaba de ganhar um PlayStaion 4 na promoção do python.org'.format(escolha))