#Developed by Henrique Treza


salario_atual = float(input("Qual o seu sálario mensal: "))
aumento = float(input("Qual seria o % de aumento que você deseja receber: "))

salario_ajustado = salario_atual + (salario_atual * (aumento /100))

print("O seu salario de {:.2f} depois do ajuste de {}% foi para {:.2f} ".format(salario_atual, aumento, salario_ajustado))