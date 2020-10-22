import Fraccion
from Fraccion import Fraccion

def llenar(matriz, columnas, filas):
    x = matriz
    m = columnas
    n = filas

    if m == n:
        for i in range(m):
            x.append([])
    else:
        for i in range(m+1):
            x.appeen([])

    for i in range(n):
        for j in range(m+1):
            x[i].append(Fraccion(int(input("Ingrese el valor: ")),1))

def resolver(matriz, columnas, filas):
    x = matriz
    m = columnas
    n = filas
    r2 = Fraccion(-1,1)
    
    for i in range(m):
        if m > n:
            if i < m-1:
                r1 = Fraccion.rec(x[i][i])
        else:
            if i < m:
                r1 = Fraccion.rec(x[i][i])

        for j in range(m,-1,-1):
            x[i][j] = x[i][j] * r1

        for k in range(n):
            for j in range(m,-1,-1):
                if i != k:
                    x[k][j] = x[k][j] + (r2 * x[k][i]) * x[i][j]

    for i in range(n):
        for j in range(m+1):
            x[i][j] = Fraccion.entero(x[i][j])

def imprimir(matriz):
    x = matriz
    for i in x:
        for elem in i:
            print(elem, end=" ")
        print()


