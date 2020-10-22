import os
"""
Autor: Gonzalez Martinez Enrique Adrian
Python 3.7


letra = ""
simbolo = "@"
espacios = 0
contador = 0

espacios = int(input("Numero de espacios: "))

while True:
        os.system("clear")
        print(simbolo)
        letra = input("Espacios, izquierda|i|, derecha|d|, salir|s|?: ")
        if letra == "d" and contador < espacios:
                simbolo = " " + simbolo
                contador += 1
        elif letra == "i" and contador > 0:
                simbolo = simbolo[1:]
                contador -= 1
        elif letra == "s":
                break
"""
def cadena(posicion, limite):
        cadena = "@"
        if posicion < limite:
                cadena = " " * posicion + "@"
        return cadena
x = cadena(6, 5)
print(x)
        

