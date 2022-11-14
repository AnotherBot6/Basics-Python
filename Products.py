print('Programa que suma los precciod de 3 productos y despliega el total')
print('Ingresa la clave del articulo A, B, C : X PARA SALIR')
Art=(input())
total=0
while Art!='X':
    if Art=='A':
        print('120')
        total=total+120
        Art=(input())
    elif Art=='B':
        print('250')
        total=total+250
        Art=(input())
    elif Art=='C':
        print('360')
        total=total+360
        Art=(input())
        
print(total)
