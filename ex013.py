# Aumento de um salario

sal = float(input('Qual o seu salario atual?'))
aum = float(0.15)

sal_final = (sal * aum) + sal

print('O seu salario com aumento ficará de {} reais'.format(sal_final))