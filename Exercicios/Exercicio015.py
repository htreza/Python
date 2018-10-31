#Developed by Henrique Treza

#Sorteia a ordem dos ganhadores dos premios
import random

nome1 = str(input('Insira  o primeiro nome: '))
nome2 = str(input('Insira o segundo nome: '))
nome3 = str(input('Insira o terceiro nome: '))
nome4 = str(input('Insira o quarto nome: '))
nome5 = str(input('Insira o quinto nome: '))

lista = [nome1, nome2, nome3, nome4, nome5]

random.shuffle(lista)

print('A ordem dos ganhadores é: ')
print(lista)
