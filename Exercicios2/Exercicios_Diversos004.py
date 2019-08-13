#Developed by Henrique Treza

##########################################################################################

while True:
    resposta = input("você gosta de mim? ")
    if resposta.upper() == "SIM":
        print("A resposta está correta!!!")
        break
    else:
        print("Opa, está não é a resposta correta!!!! Tente novamente!!!")





##########################################################################################

palavra = input("digite uma palavra: ")
reverso = " "
for letra in palavra:
    reverso = letra + reverso
    print(reverso)


##########################################################################################


for i in range(25):
    print(str(i) * i)


##########################################################################################

#Solução sem o uso de lista:

palavra = input("Digite uma palavra: ")
a = 0
e = 0
i = 0
o = 0
u = 0

for letra in palavra:
    if letra.lower() == 'a':
        a += 1
    elif letra.lower() == 'e':
        e += 1
    elif letra.lower() == 'i':
        i += 1
    elif letra.lower() == 'o':
        o += 1
    elif letra.lower() == 'u':
        u += 1

    print(f"Qtd de 'a': {a}")
    print(f"Qtd de 'e': {e}")
    print(f"Qtd de 'i': {i}")
    print(f"Qtd de 'o': {o}")
    print(f"Qtd de 'u': {u}")


########################################################################################

#Solução com o uso de lista:

palavra = input("Digite uma palavra: ")
vogais = ["a", "e", "i", "o", "u"]
contar_vogais = [0, 0, 0, 0, 0]

for letra in palavra:
    if letra.lower() in vogais:
        contador = 0
        while contador < 5:
            if letra.lower() == vogais[contador]:
                contar_vogais[contador] += 1
                contador += 1

print(f"Qtd. de 'a': {contar_vogais[0]}")
print(f"Qtd. de 'e': {contar_vogais[1]}")
print(f"Qtd. de 'i': {contar_vogais[2]}")
print(f"Qtd. de 'o': {contar_vogais[3]}")
print(f"Qtd. de 'u': {contar_vogais[4]}")

########################################################################################


while True:
    numero = input("Informe um número ou 'sair' para finalizar: ")
    if numero.lower() == "sair":
        print("Sistema finalizado.")
        break
if int(numero) % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")


########################################################################################