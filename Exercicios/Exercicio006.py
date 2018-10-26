#Developed by Henrique Treza


#Venda de produtos com Descontos

preco = float(input('Qual o valor do produto? R$'))
desconto = preco - (preco * 5/100)

print('O produto que tinha o valor de R${:.2f} e '
      'na promoção de 5% de desconto, você irá pagar somente R${}'.format(preco, desconto))


desconto10 = preco - (preco * 10/100)
print('O produto que tinha o valor de R${:.2f} e '
      'na promoção de 10% de desconto, você irá pagar somente R${}'.format(preco, desconto10))


desconto47 = preco - (preco * 47/100)
print('O produto que tinha o valor de R${:.2f} e '
      'na promoção de 47% de desconto, você irá pagar somente R${}'.format(preco, desconto47))


desconto73 = preco - (preco * 73/100)
print('O produto que tinha o valor de R${:.2f} e '
      'na promoção de 73% de desconto, você irá pagar somente R${}'.format(preco, desconto73))
