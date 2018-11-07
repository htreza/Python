# Developed by Henrique Treza

#Exercicio que fala o valor da passagem cobrando o valor por kilometragem
# Menor que 200 km valor de 0.75 pot km, acima disso 1.10 por km
viagem = float(input('Qual o distancia que o Sr(a), gostaria de ir nessa viagem: '))

if viagem <= 200:
    preco = viagem * 0.75
else:
    preco = viagem * 1.10
print('\033[032mO preço da sua passagem será de \033[mR$ {:.2f}'.format(preco))
