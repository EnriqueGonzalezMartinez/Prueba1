import os 
import time 

position = 0 
limite = 0 
direction = " " 

def move (direction, position, limite): 
    if direction == "d" and position < limite: 
        position = position + 1 
    elif direction == "i" and position > 0: 
        position = position - 1 
    return position 


def new_cadena (position): 
    cadena = "" 
    cadena = " " * position + "@" 
    return (cadena) 


limite = int (input ("¿Cuantos espacios desea agregar?: ") ) 


while direction != "s": 
    position = move (direction, position,limite) 
    cadena = new_cadena (position) 
    print (cadena) 
    direction = input ("Avanzar |" + str (limite) + "| ¿Derecha, Izquierda, Salir?: ")
    direction = direction.lower() 
    os.system("clear") 

print ("Saliendo...") 

time.sleep (3) 