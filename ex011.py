# Quantos litros de tinta preciso para pintar uma parede

altura = float(input('Qual a altura da sua parede em metros?'))
largura = float(input('Qual a largura da parede em metros?'))

m2 = largura * altura
tinta = m2 / 2

print('Para pintar a sua parede de {} quadrados, você precisará de {} litros de tinta'.format(m2, tinta))
