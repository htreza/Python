#Developed by Henrique Treza


#sistema que calcula a diaria e valor do km rodado para o cliente

qtdDia = int(input('Por quantos dia o carro foi alugado: '))
kmRodados = float(input('Quantos quilometros o sr(a) percorreu com o carro alugado: '))

valorDiaria = qtdDia * 60
valorKm = kmRodados * 0.15
valorTotal = valorDiaria + valorKm

print('O sr(a) ficou {} dias com o carro alugado e rodou {}'
      'Km, o valor total a pagar é de R${:.2f}'.format(qtdDia, kmRodados, valorTotal))
