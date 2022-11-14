def suma(Num):
    x=0
    n=1
    while n<=Num:
        x=x+n
        n=n+1
    return(x)
    

print ("Programa que suma los digitos de 0 hasta n")
Num=int(input('Ingrese un numero: '))
res =suma(Num)
print(res)
