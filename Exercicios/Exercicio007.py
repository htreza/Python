#Developed by Henrique Treza


#Aumento de salário de funcionários

salario = float(input('Qual o seu salário? R$'))

aumento = salario + (salario * 10/100)

print('Parabéns, graças ao seu esforço, seu salário que era R${:.2f} passou a ser R${:.2f} com esse ajuste de 10%'.format(salario, aumento))

aumento35 = salario + (salario * 35/100)
print('Parabéns, graças ao seu esforço, seu salário que era R${:.2f} passou a ser R${:.2f} com esse ajuste de 35%'.format(salario, aumento35))

aumento79 = salario + (salario * 79/100)
print('Parabéns, graças ao seu esforço, seu salário que era R${:.2f} passou a ser R${:.2f} com esse ajuste de 79%'.format(salario, aumento79))




