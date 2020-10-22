from playsound import playsound
from gtts import gTTS
import time
import os

"""
texto = "Hola buenas tardes"
tts = gTTS(texto, lang = "es")
tts.save("hola.mp3")
playsound("hola.mp3")
"""
#Funcion para crear un audio a partir de un documento
def audio(documento):
    with open(documento,"r") as file:
        texto = file.read()
        tts = gTTS(texto, lang = "es")
        tts.save("ejem.mp3")
        playsound("ejem.mp3")

doc = input("Ingrese la ruta del documento: ")
os.system("cls")
for i in range(2):
    print("Procesando|..")
    time.sleep(1)
    os.system("cls")
    print("Procesando.|.")
    time.sleep(1)
    os.system("cls")
    print("Procesando..|")
    time.sleep(1)
    os.system("cls")

audio(doc)



