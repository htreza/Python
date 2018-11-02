#Developed by Henrique Treza

#Exercicio que lê uma frase e mostra:
# Quantas vezes aparece a letra A
# Em que posição ela aparece na primeira vez
# Em que posição ela aparace da ultima vez


text = str(input("Insira uma frase: ")).upper().strip()
print('A letra "A" aparace {} vezes na frase, inserida acima.'.format(text.count('A')))
print('A 1° letra "A" apareceu na posição {}'.format(text.find('A')+1) )
print('A ultima letra "A" apareceu na posição {}'.format(text.rfind('A')+1))
