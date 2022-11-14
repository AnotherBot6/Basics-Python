
print("Programa que crea una matriz de minimo 2x2 y la rellena de 1 hasta n")
colum=int(input())
fila=int(input())
if colum<2 or fila<2:
    print('Error')
else:   
    matriz=[]
    c=1
    for n in range(1,colum+1):
        lista=[]
        for a in range(1,fila+1):
            lista.append(c)
            c=c+1
        matriz.append(lista)
    print(matriz)
