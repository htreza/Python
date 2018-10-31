#Developed by Henrique Treza

#Exercicio(tratar caracteres) que mostra alo inserido tudo maiusculo, minusculo e diz quantas letras tem a primeira palavra inserida.

nome = str(input('Insira seu nome completo: ')).strip()
print('Verificando seu nome: ')
print('Seu nome em maiuscula é {}'.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu nome tem {} letras'.format(nome.find(' ')))
#separa = nome.split() descobre de uma forma rapida quantas letras tem o primeiro nome
#print(separa)
#print('seu nome é {} e tem {} letras'.format(separa[0], len[0])))
