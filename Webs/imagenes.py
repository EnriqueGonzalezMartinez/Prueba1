# Enrique Adrian Gonzalez Martinez
# script que saca e imprime en pantalla los enlaces de las imagenes .jpg de una pagina web
# ‎14‎/10/‎2020, ‏‎10:48 a. m.

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.uanl.mx/enlinea'
re = requests.get(url)
soup = bs(re.content, 'html.parser')
images = soup.find_all('img', src=True)
for img in images:
    print(img)
imag = [x['src'] for x in images if x['src'].endswith('.jpg')]
for img in imag:
    print(img)
