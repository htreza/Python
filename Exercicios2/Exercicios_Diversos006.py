#Developed by Henrique Treza

##########################################################################################

numero = int(input("Qual tabuada você quer treinar? Informe o número: "))

acertos = 0
erros = 0

for n in range(1, 11):
    resposta = int(input(f"{numero} x {n} = ? "))
    if resposta == (numero * n):
        print("Você acertou Miserave!!!")
        acertos = acertos + 1
    else:
        print(f"Que peninha, você errou a tabuada!!! O valor correto é:{numero * n}")
        erros = erros + 1

        print(f"Total de acertos: {acertos}")
        print(f"Total de erros: {erros}")
