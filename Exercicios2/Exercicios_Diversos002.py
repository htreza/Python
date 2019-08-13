#Developed by Henrique Treza




########################################################

while True:
    x = input("Informe o valor de x: ")
    z = x + x
    break

print(z)


########################################################


curso = "Python para todos!"
letra = ""
for x in curso:
    letra = letra + x

print(letra)



########################################################

#Somando número do intervalo informado, limitando o maior número


inicio = int(input("Informe o primeiro número: "))
fim = int(input("Informe o número final: "))
salto = int(input("Informe o salto: "))
texto = "Cálculo: "
soma = 0
for numero in range(inicio, fim, salto):
    soma = soma + numero
    texto = texto + str(numero)
    if numero > 50:
        texto = texto + " Passou de 50"
        break
        if numero != fim-1:
            texto = texto + " + "
            print(f"{texto}")
            print(f"Soma: {soma}")

########################################################



nota = 0
qtd_notas_informadas = 0

while True:
    nota = float(input("Informe a nota (-1 para finalizar): "))
    if nota == -1:
        break
        notas = notas + nota
        qtd_notas_informadas = qtd_notas_informadas +1

        if qtd_notas_informadas > 0:
            media = notas / qtd_notas_informadas
            print(f"Quantidade de notas informadas: {qtd_notas_informadas}")
            print(f"Média: {media}")
        else:
            print("Nenhuma nota informada!!!")

