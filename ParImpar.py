#Programa que indetifica si el numero ingresado es par o impar y su signo

def main():
    import math
    num=int(input('Dame un numero '))
    
    if (num%2==0) and (num>=0):
            print('Par positivo')
    elif (num%2==0) and (num<0):
            print('Par negativo')
    elif (num%2!=0) and (num>0):
            print('Impar positivo')
    elif (num%2!=1) and(num<=0):
            print('Impar negativo')
            

if __name__ == '__main__':
    main()
