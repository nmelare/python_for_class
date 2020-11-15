n = int(input("Numero inteiro e natural: "))
while n<0 :
    n = int(input("NUmero inteiro e  natural: "))
fat = 1
for i in range(1, n+1) :
    fat *= i
print("Fatoracao = ", fat)
