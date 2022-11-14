def main():
    print("Programa que pide 2 numeros y realiza suma, resta y multiplicacion")
    A= int(input('dame un nuemero: '))
    B= int(input('dame un nuemero: '))
    
    suma=A+B
    resta=A-B
    mult=A*B
    print('La suma es: '+str(suma))
    print('La resta es: '+str(resta))
    print('La multiplicación es: '+str(mult))
    
    
if __name__ == '__main__':
    main()
