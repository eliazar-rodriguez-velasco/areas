def Cuadrado():
    l=float(input("Ingresa El Valor De Un Lado Del Cuadrado: "))
    p=(l*4)
    a=(l*l)
    print ("El Perimetro De el Cuadrado Es ",p," Metros")
    print ("El Area De el Cuadrado Es ",a," Metros Cuadrados")
Cuadrado() 

def area_triangulo(b,h):

    area=b*h/2
    return print('El area del triángulo es: ', area)

def area_trapecio(B,b,h):

    area=(B+b)*h/2
    return print('El area del Trapecio es: ', area)
