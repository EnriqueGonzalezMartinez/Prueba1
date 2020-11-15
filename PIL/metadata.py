import requests
import re
import os
from bs4 import BeautifulSoup
import argparse
from PIL import ExifTags, Image
from PIL.ExifTags import TAGS

parser = argparse.ArgumentParser()
parser.add_argument("-url", type=str, help="url del sitio web", required=True)
params = parser.parse_args()
url = params.url


def sacar_links(url):
    links = []
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'html.parser')
    etiquetas = soup.find_all('a')

    for etiqueta in etiquetas:
        url = etiqueta.get('href')
        try:
            if url.find('https') == 0:
                links.append(url)
        except:
            None
    return links


def down_image(url):
   #Expresion para buscar el inicio de la url hasta antes del ultimo '/'
   exp_url = re.compile(r'http(s)?://\w*.\w*.\w*')
   #Se busca lo anterior con el metodo search
   res = exp_url.search(url) 
   #Se encarga de transformar la url a html
   response = requests.get(url)  
   #Recibe la url
   soup = BeautifulSoup(response.content, "html.parser")
   #Busca en las imagenes en el html
   images = soup.find_all("img")
   #Se crea la carpeta images
   try:
      os.mkdir("images")
      i = 1
   except:
      with open("num_imag.txt","r") as file:
         i = file.read()
         i = int(i)
   for image in images:
      #Se guardan los enlaces en la variable t
      link = image.get("src")
      #Se crea el nombre y donde se van a guardar las imagenes
      imagename = "images" + "/" + "image" + str(i)+ ".jpg"
      #Descarga de las imagenes
      with open(imagename, "wb")as file:
         res_link = exp_url.search(link)
         try:
            res_link.group()
         except:
            link = str(res.group()) + link
         file.write(requests.get(link).content)
      # Se comprueba que la imagen se pueda abrir
      try:
         Image.open(imagename)
         print(f"Descargando imagen{i}...")
         i += 1
      except:
         os.remove(imagename)
         print("Se rechazo una imagen...")
      
   with open("num_imag.txt","w") as file:
      file.write(str(i))


def metaData(img):
    print("Sacando la metadata de imagenes...")
    # Imagename recive el path de la imagen 
    imagename = img
    # Se lee la data de la imagen
    image = Image.open(imagename)
    meta = []
    # Con el metodo getexif() obtenemos la metadata de la imagen
    exifdata = image.getexif()
    for tag_id in exifdata:
        # se consige el tag name
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        meta.append(f"{tag}: {data}\n")
    return meta
      
    
down_image(url)
#links = sacar_links(url)
#for link in links:
#   down_image(link)

images = os.listdir("images")
carpeta = os.mkdir("metadata")
for i in range(1, len(images) + 1):
    meta = metaData(f"images/image{i}.jpg")
    with open(f"metadata/metaData{i}.txt","w", encoding="utf-8") as file:
       for line in meta:
          file.write(line)
          

