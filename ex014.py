d = int(input('Quantos dias você usou o carro: '))
km = float(input('Quantos KMs você rodou: '))

cd = d * 60
ckm = km * 0.15
ct = cd + ckm

print('O valor a ser pago pelo aluguel será de R$ {}.'.format(ct))