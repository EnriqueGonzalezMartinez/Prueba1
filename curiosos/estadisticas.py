lista = ( ("Sofia",20), ("Iris",19), ("Rafael",20), ("Adrain",19), ("Adrain",17), ("Adrain",18))

def estadistica_lista(lista):    

        maximo = 0 #sirve como variable de cambio para compararse con las demas edades
        for fila in range(0,len(lista)):
                if lista[fila][1] > maximo:
                        maximo = lista[fila][1]

        minimo = 1000 #sirve como variable de cambio para compararse con las demas edades
        for fila in range(0,len(lista)):
                if lista[fila][1] < minimo:
                        minimo = lista[fila][1]

        contador = 0 #cuenta el numero de veces que es distinto el nombre a otro nombre
        nombres_unicos = 0 #cuanta el numero de nombres que son unicos
        for fila in range(0,len(lista)):
                for fila2 in range(0,len(lista)):
                        if lista[fila][0] != lista[fila2][0]:
                                contador += 1
                if contador == len(lista) - 1:
                        nombres_unicos += 1
                contador = 0

        veces = 0 #numero de veces que se repite un nombre
        contador = 0 #cuanta cuantas veces se repite un nombre
        nombre_comun = "" #Guarda el nombre mas comun de la lista
        for fila in range(0,len(lista)):
                for fila2 in range(0,len(lista)):
                        if lista[fila][0] == lista[fila2][0]:
                                contador += 1
                if contador > veces:
                        veces = contador
                        nombre_comun = lista[fila][0]
                contador = 0
                
        estadistica = (maximo, minimo, nombres_unicos, nombre_comun)
        return estadistica

resultados_estadistica = estadistica_lista(lista)
print("El rango de edad del grupo es de entre: ",resultados_estadistica[0], "y" ,resultados_estadistica[1])
print("La cantidad de nombres unicos: ", resultados_estadistica[2])
print("El nombre mas común es: ", resultados_estadistica[3])
