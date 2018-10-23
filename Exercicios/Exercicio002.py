#Recebe algo e tenha todas as informações sobre o mesmo.
# Mesmo colocando número ele irá retorna str (String)
a = input('Digite algo do seu interesse: ')
print('O tipo primitivo desse valor é: ', type(a))

#Colocando int antes do input ele lê número e não lê mais string, pois declarou que ele ira receber número.
a = int(input('Digite algo do seu interesse: '))
print('O tipo primitivo desse valor é: ', type(a))

#Saber se tem espaços em branco no campo, usuario digitou espaços em branco
a = input('Digite algo do seu interesse: ')
print('O tipo primitivo desse valor é: ', a.isspace())

#Saber se é númerico, alphanumerico, alphabeto,
a = input('Digite algo do seu interesse: ')
print('É um número: ', a.isnumeric())
print('É alfabeto: ', a.isalpha())
print('É alfanumerico: ', a.isalnum())
#Está em minusculos ou maiusculas
print('Está em maiusculas: ', a.isupper())
print('Está em minusculas: ', a.islower())
#Capitalize
print('Está capitalizada: ', a.istitle())




#Exercicio Média de aluno
nome = input('Digite seu nome: ')
n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))
media = (n1 + n2) / 2
print('Caro(a) aluno {}, com sua primeira nota {} e segunda nota {}, sua média foi {:2f}'.format(nome, n1, n2, media))  # Arredonda para duas casas decimasi {:2f} Ponto flutuante


#Exercicio Convertendo medidas

medida = float(input('Insira uma medida em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida é {} e isso em cm é {} e em mm é {}'.format(medida, cm, mm))
