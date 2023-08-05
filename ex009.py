# Tabuada


tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input("Digite um número para a tabuada: "))

for i in tab:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
