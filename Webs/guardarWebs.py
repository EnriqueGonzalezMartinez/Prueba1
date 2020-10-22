import requests
import os
import time
from bs4 import BeautifulSoup as bs

def descargarWeb(archivo):
    #se crea la ruta absoluta a la carpeta Urls
    ruta = os.path.abspath("Urls")
    #ruta para crear la carpeta PagWebs dentro de la carpeta Urls
    ruta_abs = ruta + "/PagWebs"
    #Se crea la carpeta PagWebs donde se guardaran los archivos.txt
    os.makedirs(ruta_abs, exist_ok=True)
    #Se descargan las paginas y se guarda la informacion en archivos.txt
    ruta_archivo = ruta +"/"+ archivo
    with open(ruta_archivo,"r") as file:
        num = 1
        for line in file:
            Agente = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
            page = requests.get(line, headers={"user-agent":Agente})
            if page.status_code != 200:
                continue
            #Se crea el nombre de archivo.txt
            name = "/PG%d.txt" %num
            with open(ruta_abs+name,"wb") as file2:
                file2.write(page.content)
            print("Descargando paginas web...")
            num += 1
            time.sleep(2)
    print("Hecho")

descargarWeb("urls.txt")
