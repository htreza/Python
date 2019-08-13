#Developed by Henrique Treza

###################################################################################################################################################

var = str(input('Insira um nome ou qualquer palavra (Se acertar você ganha um super premio): ')).strip()
r = (var[:12].upper() == 'CAIO GORDOLINHA')

if r:
    print('Parabens!!!!Você ganhou um super premio...Barras de Ouro, que valem mais que Dinheiro!!!')
else:
    print('Você errou, boa sorte na proxima tentativa!!!')

###################################################################################################################################################

texto1 = input("Informe o primeiro texto: ")
texto2 = input("Informe o segundo texto: ")
print("Texto 1: {}".format(texto1))
print("Texto 2: {}".format(texto2))

print(f"Quantidade de caracteres de '{texto1}': {len(texto1)} ")
print(f"Quantidade de caracteres de '{texto1}': {len(texto2)}")

print("As strings possuem a mesma quantidade de caracteres? ", len(texto1) == len(texto2))
print("As strings são iguais? ", texto1 == texto2)



###################################################################################################################################################



x = False
y = True
if x == True and y == True:
    print("x é verdadeiro e y é verdadeiro")
elif x == True and y == False:
    print("x é verdadeiro e y é falso")
elif x == False and y == False:
    print("x é falso e y é falso")
else:
    print("x é falso e y é verdadeiro")



###################################################################################################################################################


n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

resposta = float(input(f"Informe o resultado da operação: {n1} + {n2} = "))
if resposta == n1 + n2:
    print("Você acertou!!!")
else:
    print(f"Você errou. O resultado correto de {n1} + {n2} é: {n1 + n2}")

resposta = float(input(f"Informe o resultado da operação: {n1} - {n2} = "))
if resposta == n1 - n2:
    print("Você acertou!!!")
else:
    print(f"Você errou. O resultado correto de {n1} - {n2} é: {n1 - n2}")

resposta = float(input(f"Informe o resultado da operação: {n1} * {n2} = "))
if resposta == n1 * n2:
    print("Você acertou!!!")
else:
    print(f"Você errou. O resultado correto de {n1} * {n2} é: {n1 * n2}")

resp = float(input(f"Informe o resultado da operação: {n1} / {n2} = "))
if resposta == n1 / n2:
    print("Você acertou!!!")
else:
    print(f"Você errou. O resultado correto de {n1} / {n2} é: {n1 / n2}")

###################################################################################################################################################


qtd_cafe_dia = int(input("Quantas doses de café você bebe por dia: "))
cafe_final_mes = (qtd_cafe_dia * 30)

print("Você bebe {} doses de café por dia, no final do mês você bebeu {} doses de café!! ".format(qtd_cafe_dia, cafe_final_mes))

###################################################################################################################################################


















