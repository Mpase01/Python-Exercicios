# preço de um produto com desconto

preco = float(input('Qual o preço do produto? '))
porc_desc = float(input('Informe o desconto: '))

desconto = porc_desc / 100
desconto_f = preco - (preco * desconto)

print('O preço com o desconto fica {} reais'.format(desconto_f))

