#Developed by Henrique Treza

#Conversão de Temperatura

c = float(input('Informe uma temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {:.1f}°C equivale a {:.1f}°F'.format(c, f))