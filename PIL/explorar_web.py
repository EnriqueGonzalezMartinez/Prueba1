import requests
from bs4 import BeautifulSoup

def links(url):
    links = []
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'html.parser')
    etiquetas = soup.find_all('a')

    for etiqueta in etiquetas:
        url = etiqueta.get('href')
        try:
            if url.find('https') > -1:
                links.append(url)
        except:
            None

links('https://www.oracle.com/mx/index.html')