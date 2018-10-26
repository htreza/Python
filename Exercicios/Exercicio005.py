#Developed by Henrique Treza


#Cálculo do pintor, para pintar uma parede de 2m² é pintada com 1 litro de tinta

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2

print('Para pintar sua parede, você precisa ter {}litros de tinta'.format(tinta))


