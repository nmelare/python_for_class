valor = float(input("Insira valor: "))
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n2 = 0
n1 = 0
while (valor >= 100):
    n100 += 1
    valor = valor - 100
print("Notas de 100:", n100)
while (valor >= 50):
    n50 += 1
    valor = valor - 50
print("Notas de 50:", n50)
while (valor >= 20):
    n20 += 1
    valor = valor - 20
print("Notas de 20:", n20)
while (valor >= 10):
    n10 += 1
    valor = valor - 10
print("Notas de 10:", n10)
while (valor >= 2):
    n2 += 1
    valor = valor - 2
print("Notas de 2:", n2)
while (valor >= 1):
    n1 += 1
    valor = valor - 1
print("Notas de 1:", n1)
