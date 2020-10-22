from tkinter import Tk,Text,Button,END,re
from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
indice = 0

e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row = 0,column = 0,columnspan = 4, padx = 5,pady = 5)

i = 0
botones = []
valor = [1,2,3,4,5,6,7,8,9,0,"AC","(",")",".","+","-","/","*","="]

def click(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def boton(valor, escribir = True, ancho = 5, alto = 2):
    return Button(ventana, text = valor, width = ancho, height = alto, command = lambda: click(valor))

def operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

for i in range(0,len(valor)):
    if i != 10 or i != 18:
        botones.append(boton(valor[i]))

botones[10] = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: borrar())
botones[18] = Button(ventana, text = "=", width = 5, height = 2, command = lambda: operacion())
        

for i in range(1,6):
    for j in range(0,4):
        if i != 5 or j != 3:
            botones[indice].grid( row = i, column = j, padx = 5, pady = 5)
            indice += 1

ventana.mainloop()
