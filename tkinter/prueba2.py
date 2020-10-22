from tkinter import *

x = []
e = []
ventana = Tk()
filas = 2
columnas = 2
i = 0
j = 0
bandera = True

e_texto = Entry(ventana, font = ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

boton = Button(ventana, text = "Guardar", width = 5, height = 2, command = lambda: guardar())
boton.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

def guardar():
    global bandera, i, j, filas, columnas, e, boton
    
    if bandera == True:
        if columnas == filas:
            for k in range(columnas):
                x.append([])
        else:
            columnas += 1
            for k in range(columnas):
                x.appeen([])
        bandera = False
    
    x[j].append(e_texto.get())
    e_texto.delete(0, END)
    i += 1 
    if i == columnas:
        j += 1
        i = 0
    if j == columnas:
        for i in range(filas):
            e.append(texto())
        for i in range(filas):
            e[i].grid(row = i, column = 0, padx = 5, pady = 5)
            e[i].insert(0, x[i])
1        boton = Button(ventana, text = "Salir", width = 5, height = 5, command = lambda: ventana.destroy())
        boton.grid(row = filas+1, column = 0, columnspan = 2, padx = 5, pady = 5)

def texto():
    return Entry(ventana, font = ("Calibri 12"))

