import math
import random
import time


def CALCarea(radio):
    area = math.pi*radio*radio
    return area


def obtenerNumAleatorio(minimo,   maximo):
    return random.randint(minimo, maximo)


def imprimirR(MENSAJE, valor):
    print(">>", MENSAJE, "=", valor)


def procesarLISTA(lista):
    for x in lista:
        print("Elemento:", x)


def main():
    print("Iniciando   E12   con muchos errores PEP8")
    valor1 = CALCarea(5)
    imprimirR("area del circulo", valor1)
    valor2 = obtenerNumAleatorio(1, 100)
    imprimirR("numero aleatorio", valor2)
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    procesarLISTA(lista)
    if (valor1 > 0):
        print("Area positiva")
    else:
        print("Area no positiva")
    time.sleep(1)
    print("Fin del programa")


main()
