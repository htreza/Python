# Developed by Henrique Treza
# Analise de String, mostrando o primeiro e ultimo nome de uma pessoa

nome = str(input("Insira seu nome: ")).strip()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu ultimo nome é: {}'.format(n[len(n)-1]))