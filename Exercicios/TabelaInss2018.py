# Developed by Henrique Treza


# Exercicio do INSS que calcula o desconto que o funcionario tera, com o desconto de inss variando de acordo com o valor do salario

print("**************** TABELA INSS 2018 ********************")
print("* Salário de Contribuição (R$)    - Alíquota do INSS *")
print("* até 1.659,38                    -        8%        *")
print("* de 1.659,39 até 2.765,66        -        9%        *")
print("* de 2.765,67 até 5.531,31 (teto) -        11%       *")
print("******************************************************")

salario_informado = float(input("Insira o salário de contribuição: "))
salario_contribuicao = salario_informado
if (salario_contribuicao <= 1659.38):
    aliquota_inss = 8
elif (salario_contribuicao <= 2765.66 ):
    aliquota_inss = 9
elif (salario_contribuicao <= 5531.31):
    aliquota_inss = 11
else:
    salario_contribuicao = 5531.31
    aliquota_inss = 11

valor_inss = (salario_contribuicao * (aliquota_inss/100))
salario_liquido = salario_informado - valor_inss
print('O salario Informado é: R${:.2f}'
          ' A aliquota do INSS é de: {}%, '
          ' E do seu salario será descontado o valor de: R${:.2f},'
          ' E seu salario a receber, já com descontos será: R${:.2f} '.format(salario_informado, aliquota_inss, valor_inss, salario_liquido))
