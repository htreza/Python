# Developed by Henrique Treza

#Jogo do Detetive

print('Programa Detetive')
print('Responda as perguntas abaixo com S (sim) ou N (nao)')

perguntas = input('Voce telefonou para a vitima? ',
             'Voce esteve no local do crime? ',
             'Voce mora perto da vitima? ',
             'Voce devia para a vitima? ',
             'Voce trabalhou para a vitima? ')

respostas = []

for pergunta in perguntas:
    respostas.append(input(pergunta).upper())

classificacao = 0
for resposta in respostas:
    if (resposta == 'S'):
        classificacao += 1

if (classificacao < 2):
    print('Inocente')
elif (classificacao == 2):
    print('Suspeito')
elif (classificacao <= 4):
    print('Cumplice')
else:
    print('Assassino')
