#Developed by Henrique Treza


#Venda parcelada e venda no dédito

valor = float(input('Qual o valor do produto: R$ '))

debito = valor - (valor * 5/100)
parcelado = valor + (valor * 8/100)
print('O preço do produto é de R${:.2f} mas no débito ele sai com '
      'desconto de 5% e sai por R${:.2f} e no crédito o valor sofre ajuste de 8% e fica em R${:.2f} '.format(valor, debito, parcelado))

