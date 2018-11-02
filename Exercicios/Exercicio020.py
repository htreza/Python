#Developed by Henrique Treza


#Exercicio Que lê uma frase e diz se ela tem "Uma palavra que voce escolheu".
#A palavra secreta é Desenvolvedor.

var = str(input("Insira uma frase e tente acertar a palavra secreta: ")).strip()
r = ('DESENVOLVEDOR' in var.upper())

if r:
    print('Parabens!!! Você acaba de ganhar um mega premio')
else:
    print('Você errou!! Continua tentando!!')