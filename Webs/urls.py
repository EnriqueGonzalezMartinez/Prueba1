import requests, time, os, re
from bs4 import BeautifulSoup as bs

def urls(busqueda, page):
    search = "https://www.google.com/search?q=%s" %busqueda
    #saca las urls de la pagina de google
    pag = int(page+"0")
    urls = []
    for i in range(0,pag,10):
        Agente = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        response = requests.get(search+"&start=%d" %i, headers={"user-agent":Agente})
        soup = bs(response.content,"html.parser")
        links = soup.find_all('a')
        for indice in range(0,len(links)):
            link = links[indice]['href']
            inicio = link.find('http')
            if inicio != -1:
                urls.append(link[inicio:])
    print("Buscando paginas web.....")
    time.sleep(2)
    #crea la ruta absoluta a la carpeta Urls y guarda los docs.txt con las urls
    os.makedirs("Urls", exist_ok=True)
    ruta = os.path.abspath("Urls")
    with open(ruta+"/urls.txt","w") as file:
        for url in urls:
            if url.find("google") == -1:
                indice = url.find("&")
                file.write(url[:indice]+"\n")
    print("Hecho")


webs = urls("congreso de ciberseguridad 2020","2")
"""
Este script hace una busqueda en google que recibe como primer parametro
y de segundo parametro recibe el numero de paginacion en los cuales debe
sacar las urls, las urls que encuentra las escribe en un txt.
"""
