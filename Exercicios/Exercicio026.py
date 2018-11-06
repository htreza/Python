#Developed by Henrique Treza


# Exercicio que Lê 3 seguimentos de reta e diz se forma um triangulo

print('\033[034m*=\033[m'*13)
print('\033[032m Verificador de Triângulos \033[m')
print('\033[034m*=\033[m'*13)
reta1 = float(input('Insira o valor da primeira reta: '))
reta2 = float(input('Insira o valor da segunda reta: '))
reta3 = float(input('Insira o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\033[032mEsses valores de retas inseridos, formam um TRIÂNGULO\033[032m')
else:
    print('Esses valores de retas inseridos, NÃO formam um triângulo.')