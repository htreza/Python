#Developed by Henrique Treza
# Adição +
# Subtração -
# Multiplicação *
# Divisão /
# Potencia **
# Divisão inteira //
# Resto da divisão %
#Para saber oque está sendo recebido no input : print(n1.isnumeric()) isso informa se é numero ou não. print(n1.isalpha()) se ele é alfabeto.


n1 = int(input('Informe um numero: '))
n2 = int(input('Informe mais um numero: '))
soma = n1+n2
multiplicacao = n1 * n2
divisao = n1 / n2
diferenca = n1 // n2
exponenciacao = n1 ** n2
#Formato antigo do Python:  print('A soma vale', soma)

print('A soma vale {},\n o produto {} e a \n divisão {:.2f}'.format(soma, multiplicacao, divisao))
print('Divisao inteira {} e Exponenciação {}'.format(diferenca, exponenciacao))


nome = str(input('Insira  seu nome: '))
idade = int(input('Insira sua idade: '))
endereco = str(input('Insira seu endereço: '))
print('Oi, tudo bem sr(a)', nome, 'Sua idade é', idade, 'anos e seu endereço é', endereco)


#print(type(n1)) isso faz com que sabemos qual o tipo do dados recebido.
n1 = input('Digite algo: ')
print(n1.isnumeric())


nome = input('Qual o seu nome?')
print('Prazer em te conhecer {}!'.format(nome))


#Exercicio de mostrar o antecessor e sucessor do mesmo

numero = int(input('Digite um número: '))
ante = numero - 1
suce = numero + 1
print('Tendo o número {}, sabemos que seu antecessor é {} e seu sucessor é {}'.format(numero, ante, suce))


#Passando valores e tendo seu doblo, triplo e raiz
numero = int(input('Digite um número: '))
doblo = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('Os resultados do número inserido {}, \nseu doblo é g{}, \nseu triplo é {} \ne sua raiz é {}'.format(numero, doblo, triplo, raiz))