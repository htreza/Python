#Developed by Henrique Treza

#Exercicio que verifica oque voce inseriu no sistema e diz se é
# verdadeiro conforme palavra declarada como padrão: palavra usada Henrique

var = str(input('Insira um nome ou qualquer palavra (Se acertar você ganha um super premio): ')).strip()
r = (var[:8].upper() == 'HENRIQUE')

if r:
    print('Parabens!!!!Você ganhou um super premio...Barras de Ouro, que valem mais que Dinheiro!!!')
else:
    print('Você errou, boa sorte na proxima tentativa!!!')

