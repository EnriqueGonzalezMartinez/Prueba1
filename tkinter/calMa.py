from tkinter import *
from Fraccion import *
from classM import *

x = []#Lista que guarda los valores de la matriz
e = []#Lista que guarda las ventanas donde se muestran los valores de la matriz
i = 0#Variable de apoyo para llenar las matrices 
j = 0#Segunda variable de apoyo
bandera = True#Tercera variable de apoyo

ventana = Tk()#se crea la ventana principal
ventana.title("Matriz")
    
texto = Label(ventana, text = "Numero de Filas")#linea de texto dentro de la ventana
texto.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)#grid es un metdo para el formato en el que se muestra la linea de texto

e_texto = Entry(ventana)#linea de entrada de texto
e_texto.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

texto1 = Label(ventana, text = "Numero de Columnas")
texto1.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)

e_texto1 = Entry(ventana)
e_texto1.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)

boton1 = Button(ventana, text = "listo", width = 5, height = 2,  command = lambda: abrirVentana())#Button es el metodo para crear un boton en una ventana
boton1.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)

def texto12():#metodo que crea entradas de texto
    global ventana3
    return Entry(ventana3, font = ("Calibri 12"))

def llenar_matriz():
    global bandera, i, j, filas, columnas, x

    filas = int(e_texto.get())
    columnas = int(e_texto1.get())
    
    if bandera == True:
        if columnas == filas:
            for k in range(columnas):
                x.append([])
        else:
            for k in range(columnas+1):
                x.append([])
        bandera = False
        
    x[j].append(Fraccion(int(e_texto2.get()),1))
    e_texto2.delete(0, END)
    i += 1
    if i == columnas+1:
        j += 1
        i = 0
    if j == filas:
        boton1 = Button(ventana2, text = "Continuar", width = 5, height = 2, command = lambda: resolver_matriz())
        boton1.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)


    
def abrirVentana():
    global e_texto2, ventana2
    ventana.withdraw()#cierra la ventana
    ventana2 = Toplevel()#abre una nueva ventana
    texto = Label(ventana2, text = "Posicion")
    texto.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
    e_texto2 = Entry(ventana2, font = ("Calibri 20"))
    e_texto2.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
    boton2 = Button(ventana2, text = "OK", width = 5, height = 2, command = lambda: llenar_matriz())
    boton2.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)

def resolver_matriz():
    global ventana3, e
    resolver(x, columnas, filas)#metodo de la clase classM
    ventana2.withdraw()
    ventana3 = Toplevel()
    texto = Label(ventana3, text = "Resultado")
    texto.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
    #imprime la matriz ya resuelta
    for k in range(filas):
        e.append(texto12())
    for k in range(filas):
        e[k].grid(row = k, column = 0, padx = 5, pady = 5)
        indice = 0
        for h in range(columnas+1):
            e[k].insert(indice, x[k][h])#insert es un metodo para insertar en una entrada de texto una variable o cadena de texto
            indice += 1
    boton3 = Button(ventana3, text = "Salir", width = 5, height = 2, command = lambda: ventana3.destroy())
    boton3.grid(row = filas+1, column = 0, columnspan = 2, padx = 5, pady = 5)


ventana.mainloop()
