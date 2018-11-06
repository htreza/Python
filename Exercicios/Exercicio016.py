#Developed by Henrique Treza


#Sistema que lê números inseridos e diz qual é o maior e qual é menor

a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor: '))
# Verificando qual o maior número inserido
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# Verificando qual o menor número inserido
menor = b
if a < b and a < c:
    menor = a
if c < a and c < b:
    menor = c
print('O maior número inserido é o \033[034m{}\033[m'.format(maior))
print('O menor número inserido é o \033[034m{}'.format(menor))