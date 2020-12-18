import os
from PIL import Image
from PIL.ExifTags import TAGS
from PyPDF2 import PdfFileReader

def gettingMeta(path, file):
        # Se compurba que la path sea a una carpeta
        if (os.path.isdir(path)):
            # Se enlista el contenido de la carpeta
            ls = os.listdir(path)
            # Se pasa un filto para que solo queden los .jpg, .png o .pdf
            imgs = [path +'/'+ x for x in ls if x.endswith('.jpg') or x.endswith('.png')]
            pdfs = [path +'/'+ x for x in ls if x.endswith('.pdf')]
            # Se verifica que haya .jpg, .png o .pdf en las listas
            if (imgs != [] or pdfs != []):
                for img in imgs:   
                    metaImg(img, file)
                for pdf in pdfs:
                    metaPdf(pdf, file)
            else:
                print('No se encontraron .pdf, .jpg, .png en el directorio.')
        # Se comprueba que la path sea un archivo .jpg
        elif (os.path.isfile(path) and (path.endswith('.jpg') or path.endswith('.png'))):
            metaImg(path, file)
        elif (os.path.isfile(path) and path.endswith('.pdf')):
            metaPdf(path, file)
        else:
            print('La path no apunta a un archivo .pdf, .jpg o .png.')


def metaImg(path, name):
    # Se lee la data de la imagen
    image = Image.open(path)
    # Con el metodo getexif() obtenemos la metadata de la imagen
    exifdata = image.getexif()
    # Se saca el nombre de la imagen
    name1 = path[path.rfind('/') + 1:]
    meta = []
    if name == None:
        print(f"Metadata de la imagen: {name1}")
        for tag_id in exifdata:
                # se consige el tag name
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decodifica bytes 
                if isinstance(data, bytes):
                    data = data.decode()
                meta.append(f"{tag:14}: {data}")
        if (meta != []):
            for m in meta:
                print(m)
        else:
            print('No se encontro metadata.')
    else:
        try:
            with open(name,'a') as file:
                file.write(f"Metadata de la imagen: {name1}\n")
                for tag_id in exifdata:
                    # se consige el tag name
                    tag = TAGS.get(tag_id, tag_id)
                    data = exifdata.get(tag_id)
                    # decodifica bytes 
                    if isinstance(data, bytes):
                        data = data.decode()
                    meta.append(f"{tag:14}: {data}\n")
                if (meta != []):
                    for m in meta:
                        file.write(m)
                else:
                    file.write('No se encontro metadata.\n')
        except:
            print("Error al sacar la metadata.")


def metaPdf(path, name):
    pdfFile = PdfFileReader(open(path,'rb'), strict=False)
    info = pdfFile.getDocumentInfo()
    name1 = path[path.rfind('/') + 1:]
    metadata = []
    if name == None:
        print(f'Metadata del PDF: {name1}')
        for meta in info:
            metadata.append(f'{meta:14} : {info[meta]}')
        if (metadata != []):
            for m in metadata:
                print(m)
        else:
            print('No se encontro metadata.')
    else:
        try:
            with open(name,'a') as file:
                file.write(f'Metadata del PDF: {name1}\n')
                for meta in info:
                    metadata.append(f'{meta:14} : {info[meta]}\n')
                if (metadata != []):
                    for m in metadata:
                        file.write(m)
                else:
                    file.write('No se encontro metadata.')
        except:
            print("Error al sacar la metadata.")
