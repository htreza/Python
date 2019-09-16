#Developed by Henrique Treza
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

####################################################################################
#Usando uma lista dentro de outra lista

lista = [7.12, 13.6, 25.12, ["Henrique", "Fabiana", "Maria Julia", "Maria Fernanda"]]
print(lista)

nomes = lista[3]
print(nomes)

soma = lista[0] + lista[1] + lista[2]
print(soma)

####################################################################################
#Usando uma lista dentro de outra lista

letras = ["a", "b", "c", "d"]
numeros = [1, 2, 3, 4, 5]
mistura = [letras, numeros]
print(mistura)
print(mistura[0])
print(mistura[1])

####################################################################################
#Como obter o tamanho de uma lista

lista = [100, 200, 300, 7, 13, 14, 25, 33, 19, 12, 24]
tamanho = len(lista)
print(tamanho)

####################################################################################
#Obtendo o índice de um elemento da lista

linguagens = ["Python", "Salesforce", "Java", "C#", "JavaScript", "Go", "R", "PHP", "HTML", "Cobol"]
print(linguagens.index("Salesforce"))

####################################################################################
#Verificando a existência de um item na lista

linguagens = ["PYTHON", "SALESFORCE", "JAVA", "C#", "JAVASCRIPT", "GO", "R", "PHP", "HTML", "COBOL"]
linguagem = input("Informe a linguagem de programação: ")
if linguagem.upper() in linguagens:
    print(f"{linguagem.upper()} está na lista! ")
else:
    print(f"{linguagem.upper()} não está na lista! ")


####################################################################################
# Relogio Digital

#
# import tkinter as tk
# from time import strftime as time
#
# rel = tk.label(text=time("%H:%M:%S"), font="Helvetica 120 bold")
# rel.pack()
#
# def tictac():
#     now = time("%H:%M:%S")
#     if rel['text'] != now:
#             rel['text'] = now
#             rel.after(100, tictac)
#
# tictac()
# rel.mainloop()



####################################################################################
# Par ou Impar

numeros = []
lista_pares = []
lista_impares = []

while True:
    numero = int(input("Informe um número (número 0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print("Pares:", lista_pares)
print("Ímpares:", lista_impares)


####################################################################################
# Contar as palavras que foram inseridas


palavras = []

while True:
    palavra = input("Insira uma palavra (ou tecle o número 0 para sair): ")
    if palavra == "0":
        break
    palavras.append(palavra)

if palavras:
    palavra_contar = input("Informe a palavra que deseja contar: ")
    qtd = palavras.count(palavra_contar)
    print("Temos {} ocorrências de {}".format(qtd, palavra_contar))
else:
    print("Nenhuma palavra informada.")


####################################################################################
#Copiar e clonar listas

print("Copiando e clonando listas")
lista_numeros = [1, 2, 3, 4, 5]
nova_lista = lista_numeros

print(lista_numeros)
print(nova_lista)

lista_numeros += [6]
print(lista_numeros)
print(nova_lista)

nova_lista += [7]
print(lista_numeros)
print(nova_lista)

lista_numeros = [1, 2, 3, 4, 5]
lista_clonada = lista_numeros[:]
lista_clonada += [6]
print(lista_numeros)
print(lista_clonada)
lista_numeros += [7]
print(lista_numeros)
print(lista_clonada)

print("\nFatiando listas")
linguagens = ["Python", "Java", "R", "C", "C++", "Go", "JavaScript"]
linguagens2 = linguagens[3:5]
print(linguagens)
print(linguagens2)

print("\nFatiando listas")
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)
letras[2:5] = ['C', 'D', 'E']
print(letras)
letras[2:5] = []
print(letras)

####################################################################################
#Com os números inseridos, eu somo, multiplico e digo o maior e menor número


numeros = []
soma = 0
multiplicacao = 1

while True:
    numero = int(input("Insira um número (ou tecle o número 0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

if numeros:
    for numero in numeros:
        soma += numero
        multiplicacao *= numero

    numeros.sort()
    menor = numeros[0]
    maior = numeros[len(numeros)-1]

    print("Soma: ", soma)
    print("Multiplicação: ", multiplicacao)
    print("Maior número: ", maior)
    print("Menor número: ", menor)

####################################################################################


numeros = []
lista_unica = []
lista_repetidos = []

while True:
    numero = int(input("Insira um número (ou tecle o número 0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

for x in numeros:
    if x not in lista_unica:
        lista_unica.append(x)
    else:
        if x not in lista_repetidos:
            lista_repetidos.append(x)

if numeros:
    print("Números informados: ", numeros)
    print("Números sem repetição:", lista_unica)
    print("Somente números que se repetiram:", lista_repetidos)
else:
    print("Nenhum número informado!!!")


####################################################################################

