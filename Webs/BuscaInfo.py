import requests, time, os, re, json
from bs4 import BeautifulSoup as bs

def infoSig(archivo):
    informacion = []
    #expreciones regulares que buscan fecha, correo, telefono, facebook, tweeter, instagram
    mes = "Enero|Febrero|Marzo|Abril|Mayo|Junio|Julio|Agosto|Septiembre|Octubre|Noviembre|Diciembre"
    mes_abr = "Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic"
    exp1 = re.compile(r'(\d*) (%s|%s) (\d*)|(%s|%s) (\d*)( \d*)|(\d*) de (%s|%s)( de)?( \d*)?' %(mes, mes_abr,mes, mes_abr,mes, mes_abr), re.I)
    exp2 = re.compile(r'\w*@\w*.com(.mx)?')
    exp3 = re.compile(r'\(\d{2}\)\d{4}-\d{4}|\(\d{2}\) \d{4} \d{4}|\(\d{2}\)\d{8}|\d{6}-\d{4}|\d{6} \d{4}')
    exp4 = re.compile(r'facebook.com/\w*')
    exp5 = re.compile(r'tweeter.com/\w*')
    exp6 = re.compile(r'instagram.com/\w*')
    lista = [exp1,exp2,exp3,exp4,exp5,exp6]
    #abre el archivo con el codigo de la pagina
    with open(archivo,"rb") as file:
        soup = bs(file,"html.parser")
        #agrega a la lista los str que coincidan con los patrones
        for i in range(len(lista)):
            info = lista[i].search(str(soup))
            try:
                informacion.append(info.group())
            except:
                x = 0
    nombre = archivo.replace(".txt","_info.txt")
    with open(nombre,"w") as file2:
        for info in informacion:
            file2.write(info+"\n")
    print("Hecho")
        
        
        
ruta = "/home/adrian/Escritorio/Urls/PagWebs/"
files_pagwebs = os.listdir(ruta)
files_pagwebs.sort()
for file in files_pagwebs:
    archivo = ruta + file
    infoSig(archivo)

