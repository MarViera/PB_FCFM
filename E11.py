import math,random

def   SUMA (a,b):
 return a+b

def   areaCirculo (r):return math.pi*r*r

def  numeroAleatorio( minimo,   maximo ):
    x=random.randint(minimo,maximo);    return x

def imprimir_resultados(   mensaje,valor ):
 print("Resultado:",mensaje,"=",valor)

def main( ):
    print("Iniciando programa de pruebas PEP8")
    x=SUMA(  5,10 )
    imprimir_resultados("suma",x)
    y=areaCirculo(  3 )
    imprimir_resultados("area del circulo",y)
    z=numeroAleatorio(1,10)
    imprimir_resultados("numero aleatorio",z)
    if(x>0):print("La suma es positiva")
    else:print("La suma no es positiva")
    lista=[1,2,3,4,5]
    for i in lista:print("Elemento:",i)
    print("Fin del programa")

main( )
