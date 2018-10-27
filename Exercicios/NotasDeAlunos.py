#Developed by Henrique Treza

# Exercicio que fala se o aluno passou, recuperação ou está reprovado.

nome = input('Qual o seu nome: ')

nota1 = float(input('Por favor, insira sua nota do primeiro bimestre: '))

nota2 = float(input('Por favor, insira sua nota do segundo bimestre: '))

nota3 = float(input('Por favor, insira sua nota do terceiro bimestre: '))

nota4 = float(input('Por favor, insira sua nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

notas = media

if notas > 8.0:
    print('Aprovado, parabens {}, voce passou de semestre!!!'.format(nome))
elif notas < 5.0:
    print('Reprovado, {}, se esforçe mais no proximo semestre!!!'.format(nome))
else:
    print('Recuperação, {}, precisa estudar mais!!!'.format(nome))
