from hash_files import hashValuer
from metadata import gettingMeta
from webscrapin import scraping

opc = int(input("Herraminetas:\nValores Hash[0]\tMetadata de archivos(jpg, png y pdf)[1]\t"+
        "Webscrpaing[2]\n"))

herramientas = [hashValuer, gettingMeta, scraping]
target = input('Ingrese el objetivo path o web: ')
name = input('Resultado, Archivo[nombre del archivo]\tPantalla[Enter]: ')
if name == '':
    name = None

herramientas[opc](target,name)
