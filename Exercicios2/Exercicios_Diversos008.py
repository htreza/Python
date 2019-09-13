#Developed by Henrique Treza
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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


import Tkinter as tk
from time import strftime as time

rel = tk.label(text=time("%H:%M:%S"), font="Helvetica 120 bold")
rel.pack()

def tictac():
    now = time("%H:%M:%S")
    if rel['text'] != now:
            rel['text'] = now
            rel.after(100, tictac)

tictac()
rel.mainloop()
