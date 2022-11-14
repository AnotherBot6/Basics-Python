print("Programa que imprime los numero pares dentro del rango ingresado")
V_1=int(input('Valor 1: '))
V_2=int(input('Valor 2: '))
if V_1==V_2:
    print('No hay pares')
else:
    for n in range(V_1, V_2):
        if V_1%2==0:
            print(V_1)
            V_1=V_1+1
        elif V_1%2!=0:
            V_1=V_1+1
