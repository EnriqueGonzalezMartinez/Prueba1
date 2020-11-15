from PIL import ExifTags, Image
from PIL.ExifTags import TAGS
import os

def metaData(img):
    # Imagename recive el path de la imagen 
    imagename = img
    # Se lee la data de la imagen 
    image = Image.open(imagename)
    # Con el metodo getexif() obtenemos la metadata de la imagen
    exifdata = image.getexif()
    for tag_id in exifdata:
        # se consige el tag name
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        #if isinstance(data, bytes):
        #    data = data.decode()
        print(f"{imagename}")
    
    
images = os.listdir("images")
for image in images:
    metaData("images/"+ image)