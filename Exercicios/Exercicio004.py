#Developed by Henrique Treza

#Conversor de Moeda

moeda = float(input('Digite quanto você tem de dinheiro na sua carteira: '))
dolar = moeda / 3.75

print('Seu valor de R$ {:.2f} convertendo para Dolar é igual a US$ {:.2f}'.format(moeda, dolar))

moeda2 = float(input('Digite quanto você tem de dinheiro na sua carteira: '))
euro = moeda2 / 3.98

print('Seu valor em R$ {:.2f} convertendo para Euro é igual a $ {:.2f}'.format(moeda2, euro))


moeda3 = float(input('Digite quanto você tem de dinheiro na sua carteira:'))
libra = moeda3 / 4.76

print('Seu valor em R$ {:.2f} convertendo para Libra é igual a $ {:.2f}'.format(moeda3, libra))
