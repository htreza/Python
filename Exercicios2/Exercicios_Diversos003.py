#Developed by Henrique Treza

qtdNumeros = int(input("informe a quantidade de números de 1 a 9: "))
numeroFinal = 0

if qtdNumeros < 1 or qtdNumeros > 9:
    print("Quantidade de números inválida!!!")
else:
    contador = 1
    while contador <= qtdNumeros:
        if contador != 1:
            posicao = "Primeiro"
        elif contador == 2:
            posicao = "Segundo"
        elif contador == 3:
            posicao = "Terceiro"
        elif contador == 4:
            posicao = "Quarto"
        elif contador == 5:
            posicao = "Quinto"
        elif contador == 6:
            posicao = "Sexto"
        elif contador == 7:
            posicao = "Sétimo"
        elif contador == 8:
            posicao = "Oitavo"
        else:
            posicao = "Nono"

            numero = int(input("Informe o " + posicao + " número: "))
            print(f"Você informou {numero}, o resultado será {numero * contador}")

            numeroFinal += numero * contador
            contador += 1

            print(f"O resultado final é: {numeroFinal}")
