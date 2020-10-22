import os

simbolo = "@"
contadorD = 0
contadorI = 0
espacios = 0
letra = ""

espacios = int(input("Numero de espacios: "))
simbolo = "@"
# Cuenta los espacios hacia la derecha
contadorD = 0
# Cuenta los espacios hacia la izquierda
contadorI = 0

while True:
    os.system("clear")
    print(simbolo)
    letra = input("Espacios, izquierda|i|, derecha|d|, salir|s|?: ")
    if letra == "d" and contadorD != espacios:
        simbolo = " " + simbolo
        contadorD += 1
        if contadorI > 0:
            contadorI -= 1
    elif letra == "i" and contadorI != espacios:
        simbolo = simbolo[1:]
        if contadorD != 0:
            contadorI += 1
            contadorD -= 1   
    elif letra == "s":
        break
