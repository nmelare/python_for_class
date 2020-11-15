n  = int (input("Qtde de elementos?"))
while n<1 or n>20:
    print("Valor nao  valido. Digite um numero entre 1 e 20")
    n  =  int(input())
j = 1    
for i in range(n) :
    print(j**2)
    j +=1
    
