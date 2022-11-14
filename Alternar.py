#Carlos Alberto Mendoza Medina


def alternar(Num):
    x=1
    for n in range(x, Num+1,1):
        if Num%2==0:
            print(str(x),'- #')
            x=x+1
            Num=Num-1
        elif Num%2!=0:
            print(str(x),'- %')
            x=x+1
            Num=Num-1
            

def main():
    print("Programa que imprime de 0 hasta n e intercambia el signo")
    Num=int(input('Ingrese un numero: '))
    alternar(Num)




if __name__ == '__main__':
    main()
