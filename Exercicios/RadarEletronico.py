#Developed by Henrique Treza


#Radar Eletronico

#Tabela de multas
#Velocidade                                  Valor da multa          pontos      Suspensão CNH
#Até 20% acima da máxima permitida           R$ 130,16               4
#de 20% até 50% acima  da máxima permitida   R$ 195,23               5
#Superior a 50% da máxima permitida          R$ 880,41               7           Sim

velocidade_permitida = int(input('Insira a velocidade permitida na via: '))
velocidade_veiculo = int(input('Insira a velocidade que você passou no radar: '))

if velocidade_veiculo > velocidade_permitida:
    if velocidade_veiculo >= velocidade_permitida + (velocidade_permitida * (50/100)):
        valor_multa = 880.41
        pontos = 7
        suspensao = True
        descricao_multa = 'Transitar em velocidade superior a 50% da máxima permitida'
    elif velocidade_veiculo >= velocidade_permitida + (velocidade_permitida * (20 / 100)):
        valor_multa = 195.23
        pontos = 5
        suspensao = False
        descricao_multa = 'Transitar em velocidade superior à máxima permitida em 20% até 50%'
    else:
        valor_multa = 130.16
        pontos = 4
        suspensao = False
        descricao_multa = 'Transitar em velocidade superior à máxima permitida em até 20%'

    print('Você foi multado e perdeu {} pontos.'.format(pontos))
    if suspensao:
        print('Você teve a carteira suspensa.')
    print('O valor de sua multa é: R$ {:.2f}'.format(valor_multa))
    print('Motivo: {}'.format(descricao_multa))
else:
    print('Parabéns, você não foi multado.')