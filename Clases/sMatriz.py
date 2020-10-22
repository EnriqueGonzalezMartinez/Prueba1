import Fraccion
from Fraccion import Fraccion

x = [[0,0,0],[0,0,0]]

##Pide los elementos de la matriz
for i in range(0,2):
    for j in range(0,3):
        x[i][j] = Fraccion(int(input("Ingrese numero: ")),1)

r1 = Fraccion.rec(x[0][0])
r2 = Fraccion(-1,1)

##Se hace el primer 1
for z in range(2,-1,-1):
	x[0][z] = x[0][z] * r1

##Se hacen 0 abajo
for z in range(2,-1,-1):
	x[1][z]= x[1][z] + (r2*x[1][0])*x[0][z]

r3 = Fraccion.rec(x[1][1])

##Se hace el segundo 1
for z in range(2,-1,-1):
	x[1][z]= x[1][z] * r3

##Se hacen 0 arriba
for z in range(2,-1,-1):
	x[0][z]= x[0][z] + (r2*x[0][1])*x[1][z]

##Hace a las fracciones enteros
for i in range(0,2):
        for j in range(0,3):
                x[i][j] = Fraccion.entero(x[i][j])
        j = 0
        
##Imprime la matriz
for row in x:
	for elem in row:
		print(elem, end=" ")
	print()	
