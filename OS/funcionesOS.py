import os
#lista las cosas en la direccion path
print(os.listdir(path="/root/Musica"))
#
print(os.walk("Plantillas"))
#borra un archivo
os.remove("Hola Mundo.txt")
#renombra un archvio
os.rename("prueba1.txt","exito.txt")
#crea la direccion desde la carpeta hasta el archivo
print(os.path.join("/root","Programa.pdf"))
"""
os.system("xlogo")
os.system("xclock")
os.system("xeyes")
"""

