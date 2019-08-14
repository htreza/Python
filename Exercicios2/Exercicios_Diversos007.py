#Developed by Henrique Treza

####################################################################################
#Adicionar elemento em uma lista

bancos = ["C6 Bank", "Itaú", "Bradesco"]
bancos.append("Nubank")
print(bancos)

####################################################################################
#Adicionar numero em uma lista
numeros = [1, 2, 3, 4, 5, 6]
numeros.append(7)
print(numeros)

####################################################################################
#Adicionar elemento em uma lista na posição desejada

bancos = ["C6 Bank", "Itaú", "Bradesco", "Nubank", "Neon", "CEF", "Santander"]
bancos.insert(4, "Original")
print(bancos)

####################################################################################
#Remover um elemento de uma lista

bancos = ["C6 Bank", "Itaú", "Bradesco", "Nubank", "Neon", "CEF", "Santander"]
bancos.remove("Nubank")
print(bancos)

####################################################################################
#Coloca em ordem alfabetica os elementos das listas

bancos = ["C6 Bank", "Itaú", "Bradesco", "Nubank", "Neon", "CEF", "Santander"]
bancos.sort()
print(bancos)

####################################################################################
#Inverte a ordem dos elementos da lista(primeiro vai para último)

bancos = ["C6 Bank", "Itaú", "Bradesco", "Nubank", "Neon", "CEF", "Santander"]
bancos.reverse()
print(bancos)

####################################################################################
#Retorna a QTD de ocorrências de dado elemento em uma lista

todos_bancos = ["C6 Bank", "Itaú", "Bradesco", "Nubank", "Neon", "CEF", "Santander", "Original", "C6 Bank"]
qtd_c6 = todos_bancos.count("C6 Bank")
print(f"QTD de ocorrência C6 Bank:   {qtd_c6}")
numeros_a = [1, 5, 7, 8, 10, 12, 13, 14, 19, 24, 25, 33, 13, 56, 98, 7, 24, 25, 14, 12, 13, 19]
qtd_treze = numeros_a.count(13)
print(f"QTD de ocorrência do número 13:  {qtd_treze}")

####################################################################################
#Método POP retorna o elemento removido(No caso ele remove sempre o último da lista)


bancos = ["C6 Bank", "Itaú", "Bradesco", "Nubank", "Neon", "CEF", "Santander", "Original", "C6 Bank"]
banco = bancos.pop()
print(banco)

####################################################################################
#Método DEL remove um elemento da lista

linguagens = ["Python", "Salesforce", "Java", "C#", "JavaScript", "Go", "R", "PHP", "HTML", "Cobol"]
print(linguagens)
del linguagens[7]
print(linguagens)
del linguagens[3:5]
print(linguagens)

####################################################################################
#Limpar uma lista inteira ou passar o colchete vazio, tem a mesma funcionalidade da função clean

lista_livros = ["Livro 1", "Livro 2", "Livro 3", "Livro 4"]
lista_livros.clear()
print(lista_livros)

lista_livros = ["Livro 1", "Livro 2", "Livro 3", "Livro 4"]
lista_livros = []
print(lista_livros)

####################################################################################