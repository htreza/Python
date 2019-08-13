# Developed by Henrique Treza

# Jogo, o computador vai pensar em um numero random e o usuario precisa acertar esse numero, sabendo o limite min e max dos numeros

from random import randint
from time import sleep


computador = randint(1, 20) #Computador seleciona um numero entre o parametro passado
print('=.='* 20)
print('\033[32mVou pensar em um número entre 1 e 20, tente adivinhar e ganhe um super prêmio!!\033[m')
print('=.='* 20)
player = int(input('\033[34mEm que número eu pensei? \033[m')) # Player tentar adivinhar
print('Aguarde, vou pensar em um número...')
sleep(3)
if player == computador:
    print(emoji.emojize('\033[32mPARABÉNS!!! Você acaba de vencer o computador mais inteliente do mundo'
          ' e ganhou barras de ouro que vale mais que dinheiro\033[m :sunglasses:.', use_aliases=True))
else:
    print('\033[31mEu Venci, O super computador venceu!!!'
          'Eu pensei no número \033[30m{}\033[m \033[31m e não no número que você falou\033[m \033[30m{}\033[m !!!'.format(computador, player))




