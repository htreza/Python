#Developed by Henrique Treza


#Exercicio de ano bissexto

ano = int(input('Qual ano quer saber se foi bissexto ou se vai ser bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[035m O ano {} é Bissexto\033[m'.format(ano))
else:
    print('O ano não é Bissexto'.format(ano))
