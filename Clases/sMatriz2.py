import Fraccion
from Fraccion import Fraccion

x = []
r2 = Fraccion(-1,1)
m = int(input("Ingrese el numero de columnas: "))
n = int(input("Ingrese el numero de filas: "))

##Llena la matriz
if m == n:
        for i in range(0,m):
                x.append([])   
else:
        for i in range(0,m+1):
                x.append([])

for i in range(0,n):
    for j in range(0,m+1):
        x[i].append(Fraccion(int(input("Ingrese la posicion: ")),1))

##Resuelve la matriz
for i in range(0,m):
        if m > n:
                if i < m-1:
                        r1 = Fraccion.rec(x[i][i])
        else:
                if i < m:
                        r1 = Fraccion.rec(x[i][i])
        
        for j in range(m,-1,-1):
                x[i][j] = x[i][j] * r1

        for k in range(0,n):
                for j in range(m,-1,-1):
                        if i != k:
                                x[k][j] = x[k][j] + (r2*x[k][i]) * x[i][j]

##Convierte las fracciones en enteros
for i in range(0,n):
        for j in range(0,m+1):
                x[i][j] = Fraccion.entero(x[i][j])
        
##Imprime la matriz
for row in x:
	for elem in row:
		print(elem, end=" ")
	print()
