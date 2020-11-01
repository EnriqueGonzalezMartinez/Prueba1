# Enrique Adrian Gonzalez Martinez
# script que busca de forma aleatoria la cadena
# indicada e indica el timepo que tarda 
# 31/10/2020 10:11 a.m.
import random
from datetime import datetime

contra = input("Ingrese la contraseña: ")
alfabeto = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z']
cadena = ""
inicio = datetime.now()
while cadena != contra:
    cadena = ""
    for i in range(len(contra)):
        num = random.randint(0,25)
        letra = alfabeto[num]
        cadena += letra

fin = datetime.now()
tiempo = fin - inicio
print(f'Tiempo: {tiempo} Cadena: {cadena}')